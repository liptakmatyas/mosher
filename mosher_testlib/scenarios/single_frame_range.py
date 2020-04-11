import mosher

from mosher_testlib.scenarios import ExpectedResult


class Expected:
    def __init__(self, video, start_frame = 0, frame_count = 1):
        self.video = video
        self.offset = start_frame
        self.len = frame_count

        self.frame_0 = ExpectedResult(
            [self.video.segment(self.offset, 1)],
            {
                'a': [ 0, -1 ],
                'ab': [
                    (None, None), (None, 1), (None, 100),
                    (0, None), (0, 1), (0, 100),
                    (-1, None), (-1, 1), (-1, 100),
                    (-100, None), (-100, 1), (-100, 100),
                ],
                'abc': [
                    (None, None, None),
                    (None, None, 1),
                    (None, None, 2),
                    (None, None, 100),
                    (None, 1, None),
                    (None, 1, 1),
                    (None, 1, 2),
                    (None, 1, 100),
                    (None, 100, None),
                    (None, 100, 1),
                    (None, 100, 2),
                    (None, 100, 100),
                    (None, -100, -1),
                    (None, -100, -2),
                    (None, -100, -100),
                    (0, None, None),
                    (0, None, 1),
                    (0, None, 2),
                    (0, None, 100),
                    (0, 1, None),
                    (0, 1, 1),
                    (0, 1, 2),
                    (0, 1, 100),
                    (0, 100, None),
                    (0, 100, 1),
                    (0, 100, 2),
                    (0, 100, 100),
                    (0, -100, -1),
                    (0, -100, -2),
                    (0, -100, -100),
                    (1, -100, -1),
                    (1, -100, -2),
                    (1, -100, -100),
                    (100, -100, -1),
                    (100, -100, -2),
                    (100, -100, -100),
                    (-1, None, None),
                    (-1, None, 1),
                    (-1, None, 2),
                    (-1, None, 100),
                    (-1, 1, None),
                    (-1, 1, 1),
                    (-1, 1, 2),
                    (-1, 1, 100),
                    (-1, 100, None),
                    (-1, 100, 1),
                    (-1, 100, 2),
                    (-1, 100, 100),
                    (-1, -100, -1),
                    (-1, -100, -2),
                    (-1, -100, -100),
                    (-100, None, None),
                    (-100, None, 1),
                    (-100, None, 2),
                    (-100, None, 100),
                    (-100, 1, None),
                    (-100, 1, 1),
                    (-100, 1, 2),
                    (-100, 1, 100),
                    (-100, 100, None),
                    (-100, 100, 1),
                    (-100, 100, 2),
                    (-100, 100, 100),
                ],
            }
        )

        self.frame_0_twice = ExpectedResult(
            [self.video.segment(self.offset, 1),
             self.video.segment(self.offset, 1)],
            {
                'tuple': [
                    (x, y)
                    for x in [None, 0, -1]
                    for y in [None, 0, -1]
                ],
            }
        )

        self.frame_0_thrice = ExpectedResult(
            [self.video.segment(self.offset, 1),
             self.video.segment(self.offset, 1),
             self.video.segment(self.offset, 1)],
            {
                'tuple': [
                    (x, y, z)
                    for x in [None, 0, -1]
                    for y in [None, 0, -1]
                    for z in [None, 0, -1]
                ] + [
                    (x, (y, z))
                    for x in [None, 0, -1]
                    for y in [None, 0, -1]
                    for z in [None, 0, -1]
                ] + [
                    ((x, y), z)
                    for x in [None, 0, -1]
                    for y in [None, 0, -1]
                    for z in [None, 0, -1]
                ],
            }
        )

        self.frame_0_four_times = ExpectedResult(
            [self.video.segment(self.offset, 1),
             self.video.segment(self.offset, 1),
             self.video.segment(self.offset, 1),
             self.video.segment(self.offset, 1)],
            {
                'tuple': [
                    ((w, x), (y, z))
                    for w in [None, 0, -1]
                    for x in [None, 0, -1]
                    for y in [None, 0, -1]
                    for z in [None, 0, -1]
                ],
            }
        )

        self.full_range = self.frame_0

        print(self.frame_0_twice.non_empty)
        self.non_empty = {
            'a': { **self.frame_0.non_empty['a'] },
            'ab': { **self.frame_0.non_empty['ab'] },
            'abc': { **self.frame_0.non_empty['abc'] },
            'tuple': {
                **self.frame_0_twice.non_empty['tuple'],
                **self.frame_0_thrice.non_empty['tuple'],
                **self.frame_0_four_times.non_empty['tuple'],
            },
        }

indices = {
    'a': [0, -1, 1, -2],
    'ab': {
        'a': [None, 0, 1, 100, -1, -100],
        'b': [None, 0, 1, 100, -1, -100],
    },
    'abc': {
        'a': [None, 0, 1, 100, -1, -100],
        'b': [None, 0, 1, 100, -1, -100],
        'c': [None, 0, 1, 2, 100, -1, -2, -100],
    },
    'tuple': [
        (x, y)
        for x in [None, 0, -1]
        for y in [None, 0, -1]
    ] + [
        (x, y)
        for x in [0, -1, (0, 0), (0, -1), (-1, 0), (-1, -1)]
        for y in [0, -1, (0, 0), (0, -1), (-1, 0), (-1, -1)]
    ]
}

#   mosher_testlib.scenarios.single_frame_range.at_the_beginning(video)
def at_the_beginning(video):
    #   Create a single-frame frame range at the beginning of the video
    video_range = (video, 0, 1)
    frame_range = mosher.FrameRange(*video_range)
    expected = Expected(*video_range)

    return (frame_range, indices, expected)


def in_the_middle(video):
    #   Create a single-frame frame range in the middle of the video
    video_range = (video, 10, 1)
    frame_range = mosher.FrameRange(*video_range)
    expected = Expected(*video_range)

    return (frame_range, indices, expected)

