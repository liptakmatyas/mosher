import re
import subprocess

import mosher


class Video:

    def __init__(self, idx, input_file):
        self._idx = idx
        self._input_file = input_file

        self._iframe = None
        self._pframe = None

        self._ffprobe = {
            'frame_count': {
                'stream': 'nb_frames',
                'parse_output': self._ffprobe_nb_frames_parser,
                'value': None,
            },
            'frame_duration_s': {
                'stream': 'r_frame_rate',
                'parse_output': self._ffprobe_r_frame_rate_parser,
                'value': None,
            },
        }

    def _ffprobe_entry(self, entry):
        if self._ffprobe[entry]['value'] is None:
            ffprobe_cmd = [
                'ffprobe',
                '-v', 'error',
                '-select_streams', 'v:0',
                '-show_entries', 'stream={}'.format(self._ffprobe[entry]['stream']),
                '-of', 'default=nokey=1:noprint_wrappers=1',
                self._input_file
            ]
            ffprobe = subprocess.run(ffprobe_cmd, stdout=subprocess.PIPE)
            self._ffprobe[entry]['value'] = self._ffprobe[entry]['parse_output'](ffprobe.stdout)

        return self._ffprobe[entry]['value']

    def _ffprobe_nb_frames_parser(self, frame_count):
        return int(frame_count)

    def _ffprobe_r_frame_rate_parser(self, fps_fraction):
        #   The output is FPS in "a/b" form, i.e. as a fraction
        #   Frame duration is 1/fps
        fps = fps_fraction.decode("utf-8").strip()
        m = re.match(r"(\d+)/(\d+)", fps)
        if m is None:
            raise ValueError("unexpected frame rate format: {}".format(fps))

        nom, denom = m.groups()
        return float(denom) / float(nom)

    @property
    def frame_duration_s(self):
        return self._ffprobe_entry('frame_duration_s')

    @property
    def frame_count(self):
        return self._ffprobe_entry('frame_count')

    @property
    def frame_duration_us(self):
        return self.frame_duration_s * 10**6

    def segment(self, start_frame, frame_count):
        return {
            'video_idx': self._idx,
            'video_start_frame': start_frame,
            'video_frame_count': frame_count,
            'start_us': start_frame * self.frame_duration_us,
            'duration_us': frame_count * self.frame_duration_us,
        }

    @property
    def I(self):
        """Get the I-frame as a FrameRange

        The range is 1 frame long, so only index 0 works (and its equivalents).
        """
        if self._iframe is None:
            self._iframe = mosher.FrameRange(self, 0, 1)
        return self._iframe

    @property
    def P(self):
        """Get P-frames as a FrameRange

        P-frames are indexed from 0.
        P[0] is the second frame of the video.
        """
        if self._pframe is None:
            self._pframe = mosher.FrameRange(self, 1, self.frame_count - 1)
        return self._pframe

