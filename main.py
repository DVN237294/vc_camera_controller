"""
    VcCameraControl. Camera control service for Virtual Classroom Project

Usage:
    vccamera <room> <vc_username> <vc_password> [-v...] [options]

Options:
    -h, --help                          Print this help text
    -v                                  Set the loglevel

Operations:
Config:
    --mem-buffer-size <value>           Set the size of the memory buffer, in bytes, when recording [default: 536870912]
"""
import logging
from time import sleep
from docopt import docopt
from picam_interfaces import PiCamInterface
from fractions import Fraction
from datetime import datetime, timedelta
from record_handler import RecordHandler
import openapi_client
import schedule

class Program:
    def __init__(self):
        self._cam = None
        self._api_conf = None
        self._api_client = None
        self._auth_api = None
        self._schedule_api = None
        self._log = logging.getLogger(__name__)
        self._args = None


    def main(self):
        self._args = docopt(__doc__)
        logging.basicConfig(level=-10 * self._args["-v"] + 30)

        self._cam = PiCamInterface()
        self._api_conf = openapi_client.Configuration(host="https://192.168.1.111:44388")
        self._api_conf.verify_ssl = False
        self._api_client = openapi_client.ApiClient(configuration=self._api_conf)
        self._auth_api = openapi_client.AuthenticationApi(self._api_client)
        self._schedule_api = openapi_client.ScheduleApi(self._api_client)
        self._video_upload_api = openapi_client.VideostreamApi(self._api_client)
        self._recorder = RecordHandler(ul_api=self._video_upload_api, buffer_size=int(self._args["--mem-buffer-size"])) 
        
        auth_token = self._get_jwt_token(self._args["<vc_username>"], self._args["<vc_password>"])
        if auth_token:
            self._api_conf.access_token = auth_token
            self._log.debug("Authorized as %s with JWT token %s" % (self._args["<vc_username>"], auth_token))
        else:
            self._log.error("Unable to authenticate as %s. Exiting.." % self._args["<vc_username>"])
            exit(1)

        self._update_schedule_jobs()
        schedule.jobs[0].run()
        sleep(10)
        schedule.jobs[1].run()
        schedule.every().day.at("06:00").do(self._update_schedule_jobs)

        while True:
            schedule.run_pending()
            sleep(1)

    
    def _update_schedule_jobs(self):
        room_schedule = self._schedule_api.api_schedule_for_room_room_name_get(room_name=self._args["<room>"],
            start_utc=datetime.utcnow(),
            end_utc=datetime.utcnow() + timedelta(days=1))
        
        for session in room_schedule.scheduled_sessions:
            if self._sanitize_dates(session):
                if session.start_time and session.end_time and session.end_time > session.start_time:
                    self._schedule_session_handler(self._start_recording_job, session.start_time, session)
                    self._schedule_session_handler(self._stop_recording_job, session.end_time, session)
                else:
                    self._log.warning("Schduled session has inconsistent schedule time: %s -> %s" 
                    % (str(session.start_time), str(session.end_time)))

    def _schedule_session_handler(self, handler, runtime, session):
        # Bit of a hack on the schedule module
        job = schedule.every().day.do(handler, session)
        job.tag(session.id)
        job.next_run = runtime

    def _start_recording_job(self, session):
        self._log.info("Starting recording of session %s" % str(session))
        self._recorder.record_session(self._cam, session)

    def _stop_recording_job(self, session):
        self._log.info("Ending recording of session %s" % str(session))
        self._recorder.end_session_recording(session)

    def _sanitize_dates(self, session):
        if not isinstance(session.start_time, datetime):
            try:
                session.start_time = datetime.strptime(session.start_time, '%Y-%m-%dT%H:%M:%S')
            except ValueError:
                self._log.error("Unable to parse date string from API: %s" % session.start_time)
                return False
        if not isinstance(session.end_time, datetime):
            try:
                session.end_time = datetime.strptime(session.end_time, '%Y-%m-%dT%H:%M:%S')
            except ValueError:
                self._log.error("Unable to parse date string from API: %s" % session.end_time)
                return False
        return True

    def _get_jwt_token(self, username, password):
        try:
            login_rsp = self._auth_api.api_authentication_post(
                login_model=openapi_client.LoginModel(user_name=username, password=password))
            return login_rsp.token
        except openapi_client.ApiException as e:
            self._log.exception("Exception when calling AuthenticationApi->api_authentication_post: %s\n" % e)



if __name__ == '__main__':
    Program().main()
        