from picamera import PiCamera 

class PiCamInterface:
    def __init__(self):
        self.cam = PiCamera(
            resolution = (1280, 720),
            framerate = 25
        )
        self._recording = False

    def record_to_stream(self, stream):
        if self._recording:
            raise NotImplementedError("PiCamInterface can only record one thing at a time")

        self.cam.start_recording(stream, format='h264', quality=25)

    def stop_recording(self):
        self.cam.stop_recording()
        self._recording = False