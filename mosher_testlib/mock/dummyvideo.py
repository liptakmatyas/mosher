class DummyVideo():

    def __init__(self, idx = None, input_file = None, fps = None):
        self._idx = idx
        self._input_file = input_file
        self._fps = fps

    @property
    def frame_duration_us(self):
        return (1.0 / self._fps) * 10**6 # 25 FPS in microseconds

    def segment(self, start_frame, frame_count):
        return {
            'video_idx': self._idx,
            'video_start_frame': start_frame,
            'video_frame_count': frame_count,
            'start_us': start_frame * self.frame_duration_us,
            'duration_us': frame_count * self.frame_duration_us,
        }

