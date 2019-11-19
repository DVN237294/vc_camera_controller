import tempfile
from openapi_client import Video, VideoProperties
from datetime import datetime

class RecordingException(Exception):
    pass

class RecordHandler:
    def __init__(self, ul_api, *args, **kvargs):
        self._upload_api = ul_api
        self._recordings = dict()

        if "buffer_size" in kvargs and isinstance(kvargs["buffer_size"], int):
            self._buffer_size = kvargs["buffer_size"]
        else:
            self._buffer_size = 536870912  # 512 MiB

    def record_session(self, cam_intf, session):
        if session.id in self._recordings:
            raise RecordingException("This session is already being recorded")
        
        stream = tempfile.SpooledTemporaryFile(max_size=self._buffer_size, mode="w+b")
        self._recordings[session.id] = (cam_intf, stream, datetime.utcnow())
        cam_intf.record_to_stream(stream)

    def end_session_recording(self, session):
        cam_intf, stream, start_time = self._recordings[session.id]

        duration = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        cam_intf.stop_recording()
        video = Video(
                properties=VideoProperties(
                    width=1280,
                    height=720,
                    file_size=None,  # to be determined
                    mime_type="video/mp4",  # to be determined
                    duration=duration,
                    container_ext=".h264"  # sort of to be determined
                ),
                name = "wut",
                thumbnail_url=None,  # to be determined
                record_time_utc=session.start_time
            )

        try:
            ul_token = self._upload_api.api_videostream_post(video=video)
            self._upload_api.api_videostream_ul_token_post(ul_token=ul_token, file=[stream._file])
        finally:
            stream.close()