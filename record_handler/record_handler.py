import tempfile
from openapi_client import Video, VideoProperties
from datetime import datetime
import ffmpeg
import logging

class RecordingException(Exception):
    pass

class RecordHandler:
    def __init__(self, video_intf, audio_intf, ul_api, *args, **kvargs):
        self._upload_api = ul_api
        self._recordings = dict()
        self._video_intf = video_intf
        self._audio_intf = audio_intf
        self._log = logging.getLogger(__name__)

        if "buffer_size" in kvargs and isinstance(kvargs["buffer_size"], int):
            self._buffer_size = kvargs["buffer_size"]
        else:
            self._buffer_size = 536870912  # 512 MiB

    def record_session(self, session):
        if session.id in self._recordings:
            raise RecordingException("This session is already being recorded")
        
        video_stream = None
        audio_stream = None
        
        self._log.debug("Starting recording of session id %d", session.id)
        if self._video_intf:
            video_stream = tempfile.SpooledTemporaryFile(max_size=self._buffer_size, mode="w+b")
            self._video_intf.record_to_stream(video_stream)
            self._log.debug("Recording video of session id %d with video interface %s", session.id, self._video_intf.__class__.__name__)
        if self._audio_intf:
            audio_stream = tempfile.SpooledTemporaryFile(max_size=self._buffer_size, mode="w+b")
            self._audio_intf.record_to_stream(audio_stream)
            self._log.debug("Recording audio of session id %d with audio interface %s", session.id, self._audio_intf.__class__.__name__)

        self._recordings[session.id] = (video_stream, audio_stream, datetime.utcnow())

    def end_session_recording(self, session, **kwargs):
        video_stream, audio_stream, start_time = self._recordings[session.id]
        del self._recordings[session.id]

        self._log.debug("Ending recording of session id %d", session.id)
        if self._video_intf:
            self._video_intf.stop_recording()
        if self._audio_intf:
            self._audio_intf.stop_recording()

        output_file = tempfile.NamedTemporaryFile(mode="w+b")
        try:
            (
                ffmpeg.input('pipe:')
                .output(output_file.name, codec="copy", format="mp4")
                .global_args('-y')
                .run(input=video_stream._file.getvalue(), capture_stderr=True)
            )
        except ffmpeg.Error:
            self._log.exception("Failed to produce video for session %d. ffmpeg produced error:", session.id, exc_info=True)
            return
        finally:
            if video_stream:
                video_stream.close()
            if audio_stream:
                audio_stream.close()

        video_details = ffmpeg.probe(output_file.name)
        self._log.debug("Session recording produced video with the following details:\n%s", video_details)
        video_stream_details = next(filter(lambda s: s['codec_type'] == 'video', video_details['streams']))
        video_name = self._format_video_name(session, kwargs['videoname'])
        video = Video(
                properties=VideoProperties(
                    width=video_stream_details['width'],
                    height=video_stream_details['height'],
                    file_size=int(video_details['format']['size']), 
                    mime_type="video/mp4",
                    duration=int(float(video_details['format']['duration']) * 1000),
                    container_ext="mp4"
                ),
                name = video_name,
                thumbnail_url=None,  # to be determined
                record_time_utc=start_time
            )

        try:
            ul_token = self._upload_api.api_videostream_post(video=video)
            if ul_token and ul_token.ul_token:
                video = self._upload_api.api_videostream_ul_token_post(ul_token=ul_token.ul_token, file=[output_file.name])
                self._log.info("Successfully uploaded video \"%s\" with id %d for session %d", video.name, video.id, session.id)
        finally:
            output_file.close()

    def _format_video_name(self, session, name):
        attrs = {'cn': '', 'st': ''}
        if '{st}' in name:
            if not session.start_time:
                self._log.warning("Session start time specified in name predicate, but session had no start time.")
            else:
                attrs.update({'st': str(session.start_time)})

        if '{cn}' in name:
            if not (session.course and session.course.name):
                self._log.warning("Session course name specified in name predicate, but session had no course name.")
            else:
                attrs.update({'cn': session.course.name})
            
        return name.format(**attrs)