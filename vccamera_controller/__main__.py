"""
    Vc Camera Controller. Camera controller service for Virtual Classroom Project

Usage:
    vccamera <vc_username> <vc_password> [-v...] [options]

Options:
    -h, --help                          Print this help text
    -v                                  Set the loglevel
    --video-name <name>                 Set the video name predicate of produced video [default: {cn} - {st}]
                                        (cn: course name, st: start time)

Operations:
    --monitor-room-schedule <room>      Record lectures scheduled for a given room
    --record-now <seconds>              Record now for given amount of seconds and post video

Config:
    --mem-buffer-size <value>           Set the size of the memory buffer, in bytes, when recording [default: 536870912]
    --api-url <url>                     Url of the api to use [default: vc-api.amavin.dk]
    --no-verify-certs                   Disables certificate validation of the https api endpoint 
"""
import logging
from time import sleep
from docopt import docopt
from camera_interface import PiCamInterface
from fractions import Fraction
from datetime import datetime, timedelta
from record_handler import RecordHandler
import openapi_client
import schedule

class VcCameraController:
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

        if not (self._args["--monitor-room-schedule"] or self._args["--record-now"]):
            self._log.error("Please provide an operation option")
            exit(1)

        self._cam = PiCamInterface()
        self._api_conf = openapi_client.Configuration(host=self._args["--api-url"])
        self._api_conf.verify_ssl = False if self._args["--no-verify-certs"] else True
        self._api_client = openapi_client.ApiClient(configuration=self._api_conf)
        self._auth_api = openapi_client.AuthenticationApi(self._api_client)
        self._schedule_api = openapi_client.ScheduleApi(self._api_client)
        self._video_upload_api = openapi_client.VideostreamApi(self._api_client)
        self._recorder = RecordHandler(ul_api=self._video_upload_api,
                                        video_intf=self._cam,
                                        audio_intf=None,
                                        buffer_size=int(self._args["--mem-buffer-size"])) 
        
        auth_token = self._get_jwt_token(self._args["<vc_username>"], self._args["<vc_password>"])
        if auth_token:
            self._api_conf.access_token = auth_token
            self._log.debug("Authorized as %s with JWT token %s" % (self._args["<vc_username>"], auth_token))
        else:
            self._log.error("Unable to authenticate as %s. Exiting.." % self._args["<vc_username>"])
            exit(1)

        if self._args["--record-now"]:
            self._start_recording_now(int(self._args["--record-now"]))
            
        if self._args["--monitor-room-schedule"]:
            self._log.info("Recording sessions upcoming in room %s indefinitely. Ctrl-C to terminate", self._args["--monitor-room-schedule"])
            if self._update_schedule_jobs():
                schedule.every().day.at("06:00").do(self._update_schedule_jobs)
                
                while True:
                    schedule.run_pending()
                    sleep(5)

    def _update_schedule_jobs(self):
        try:
            room_schedule = self._schedule_api.api_schedule_for_room_room_name_get(room_name=self._args["--monitor-room-schedule"],
                start_utc=datetime.utcnow(),
                end_utc=datetime.utcnow() + timedelta(days=1))
        except openapi_client.ApiException as ex:
            if ex.status == 404:
                self._log.error("The given room \"%s\" was not found.", self._args["--monitor-room-schedule"])
                return False
            raise
        
        self._log.info("Updating recording schedule of room %s", self._args["--monitor-room-schedule"])
        self._log.info("Room has %d upcoming sessions.", len(room_schedule.scheduled_sessions))
        
        for session in room_schedule.scheduled_sessions:
            if self._sanitize_dates(session):
                if session.start_time and session.end_time and session.end_time > session.start_time:
                    self._log.debug("Scheduling recording of session %d with subject \"%s\" starting at %s", session.id, session.course.name, str(session.start_time))
                    self._schedule_session_handler(self._start_recording_job, session.start_time, session)
                    self._schedule_session_handler(self._stop_recording_job, session.end_time, session)
                else:
                    self._log.warning("Schduled session has inconsistent schedule time: %s -> %s. Session was ignored." 
                    % (str(session.start_time), str(session.end_time)))

        return True

    def _start_recording_now(self, seconds):
        self._log.info("Recording right now, for %s seconds.", seconds)
        dummy_session = openapi_client.ScheduledSession(
            id=0, 
            webuntis_id=1, 
            webuntis_course_id=1, 
            room_id=1, 
            start_time=str(datetime.now()),
            end_time=datetime.now() + timedelta(seconds=seconds))
        self._recorder.record_session(dummy_session)
        sleep(seconds)
        self._recorder.end_session_recording(dummy_session, videoname=self._args["--video-name"])

    def _schedule_session_handler(self, handler, runtime, session):
        # Bit of a hack on the schedule module
        job = schedule.every().day.do(handler, session)
        job.tag(session.id)
        job.next_run = runtime

    def _start_recording_job(self, session):
        self._recorder.record_session(session)
        return schedule.CancelJob()

    def _stop_recording_job(self, session):
        self._recorder.end_session_recording(session, videoname=self._args["--video-name"])
        return schedule.CancelJob()

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


def main():
    VcCameraController().main()

#VcCameraController().main()