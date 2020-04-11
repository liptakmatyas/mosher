import mosher

from mosher_testlib.scenarios import ExpectedResult


class Expected:
    def __init__(self, video, start_frame = 0, frame_count = 1):
        self.video = video
        self.offset = start_frame
        self.len = frame_count

        self.frame_0 = ExpectedResult(
            [video.segment(self.offset + 0, 1)],
            {
                'a': [ 0, -5 ],
                'ab': [
                    (0, 1),
                    (-100, 1),
                    (None, 1),
                ],
                'abc': [
                    (None, None, 100),
                    (None, 1, None),
                    (None, 1, 1),
                    (None, 1, 2),
                    (None, 1, 100),
                    (None, 100, 100),
                    (None, -1, 100),
                    (None, -100, -1),
                    (None, -100, -2),
                    (None, -100, -100),
                    (0, None, 100),
                    (0, 1, None),
                    (0, 1, 1),
                    (0, 1, 2),
                    (0, 1, 100),
                    (0, 100, 100),
                    (0, -1, 100),
                    (0, -100, -1),
                    (0, -100, -2),
                    (0, -100, -100),
                    (-100, None, 100),
                    (-100, 1, None),
                    (-100, 1, 1),
                    (-100, 1, 2),
                    (-100, 1, 100),
                    (-100, 100, 100),
                    (-100, -1, 100),
                ]
            }
        )

        self.frame_0_twice = ExpectedResult(
            [self.video.segment(self.offset, 1),
             self.video.segment(self.offset, 1)],
            {
                'tuple': [
                    (x, y)
                    for x in [0, -5]
                    for y in [0, -5]
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
                    for x in [0, -5]
                    for y in [0, -5]
                    for z in [0, -5]
                ] + [
                    (x, (y, z))
                    for x in [0, -5]
                    for y in [0, -5]
                    for z in [0, -5]
                ] + [
                    ((x, y), z)
                    for x in [0, -5]
                    for y in [0, -5]
                    for z in [0, -5]
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
                    for w in [0, -5]
                    for x in [0, -5]
                    for y in [0, -5]
                    for z in [0, -5]
                ],
            }
        )

        self.frame_1 = ExpectedResult(
            [video.segment(self.offset + 1, 1)],
            {
                'abc': [
                    (1, None, 100),
                    (1, 0, -1),
                    (1, 0, -2),
                    (1, 0, -100),
                    (1, 100, 100),
                    (1, -1, 100),
                    (1, -100, -2),
                    (1, -100, -100),
                ]
            }
        )

        self.frame_1_twice = ExpectedResult(
            [video.segment(self.offset + 1, 1),
             video.segment(self.offset + 1, 1)],
            {
                'tuple': [
                    (1, 1),
                ]
            }
        )

        self.frame_4 = ExpectedResult(
            [video.segment(self.offset + 4, 1)],
            {
                'a': [ 4, -1 ],
                'ab': [
                    (-1, 100),
                    (-1, None),
                ],
                'abc': [
                    (100, 0, -100),
                    (100, 1, -100),
                    (100, -100, -100),
                    (-1, None, None),
                    (-1, None, 1),
                    (-1, None, 2),
                    (-1, None, 100),
                    (-1, 0, -100),
                    (-1, 1, -100),
                    (-1, 100, None),
                    (-1, 100, 1),
                    (-1, 100, 2),
                    (-1, 100, 100),
                    (-1, -100, -100),
                ]
            }
        )

        self.frame_0_1 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [0, 1]],
            {
                'tuple': [
                    (0, 1),
                    (-5, 1),
                ]
            }
        )

        self.frame_0_2 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [0, 2]],
            {
                'abc': [
                    (None, -1, 2),
                    (0, -1, 2),
                    (-100, -1, 2),
                ]
            }
        )

        self.frame_0_4 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [0, 4]],
            {
                'tuple': [
                    (0, 4),
                    (0, -1),
                    (-5, 4),
                    (-5, -1),
                ],
            }
        )

        self.frame_1_0 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [1, 0]],
            {
                'abc': [
                    (1, -100, -1),
                ],
                'tuple': [
                    (1, 0),
                    (1, -5),
                ],
            }
        )

        self.frame_1_3 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [1, 3]],
            {
                'abc': [
                    (1, None, 2),
                    (1, 100, 2),
                    (1, -1, 2),
                ]
            }
        )

        self.frame_1_4 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [1, 4]],
            {
                'tuple': [
                    (1, 4),
                    (1, -1),
                ],
            }
        )

        self.frame_4_0 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [4, 0]],
            {
                'tuple': [
                    (4, 0),
                    (4, -5),
                    (-1, 0),
                    (-1, -5),
                ]
            }
        )

        self.frame_4_1 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [4, 1]],
            {
                'tuple': [
                    (4, 1),
                    (-1, 1),
                ]
            }
        )

        self.frame_4_2 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [4, 2]],
            {
                'abc': [
                    (100, 0, -2),
                    (100, 1, -2),
                    (-1, 0, -2),
                    (-1, 1, -2),
                ]
            }
        )

        self.frame_4_twice = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [4, 4]],
            {
                'tuple': [
                    (x, y)
                    for x in [4, -1]
                    for y in [4, -1]
                ],
            }
        )

        self.frame_4_to_0 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [4, 3, 2, 1, 0]],
            {
                'abc': [
                    (100, -100, -1),
                    (-1, -100, -1),
                ]
            }
        )

        self.frame_4_to_1 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [4, 3, 2, 1]],
            {
                'abc': [
                    (100, 0, -1),
                    (-1, 0, -1),
                ]
            }
        )

        self.frame_4_to_2 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [4, 3, 2]],
            {
                'abc': [
                    (100, 1, -1),
                    (-1, 1, -1),
                ]
            }
        )

        self.frame_0_0_4 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [0, 0, 4]],
            {
                'tuple': [
                    (x, y, z)
                    for x in [0, -5]
                    for y in [0, -5]
                    for z in [4, -1]
                ] + [
                    (x, (y, z))
                    for x in [0, -5]
                    for y in [0, -5]
                    for z in [4, -1]
                ] + [
                    ((x, y), z)
                    for x in [0, -5]
                    for y in [0, -5]
                    for z in [4, -1]
                ]
            }
        )

        self.frame_0_4_0 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [0, 4, 0]],
            {
                'tuple': [
                    (x, y, z)
                    for x in [0, -5]
                    for y in [4, -1]
                    for z in [0, -5]
                ] + [
                    (x, (y, z))
                    for x in [0, -5]
                    for y in [4, -1]
                    for z in [0, -5]
                ] + [
                    ((x, y), z)
                    for x in [0, -5]
                    for y in [4, -1]
                    for z in [0, -5]
                ]
            }
        )

        self.frame_0_4_4 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [0, 4, 4]],
            {
                'tuple': [
                    (x, y, z)
                    for x in [0, -5]
                    for y in [4, -1]
                    for z in [4, -1]
                ] + [
                    (x, (y, z))
                    for x in [0, -5]
                    for y in [4, -1]
                    for z in [4, -1]
                ] + [
                    ((x, y), z)
                    for x in [0, -5]
                    for y in [4, -1]
                    for z in [4, -1]
                ]
            }
        )

        self.frame_4_0_0 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [4, 0, 0]],
            {
                'tuple': [
                    (x, y, z)
                    for x in [4, -1]
                    for y in [0, -5]
                    for z in [0, -5]
                ] + [
                    (x, (y, z))
                    for x in [4, -1]
                    for y in [0, -5]
                    for z in [0, -5]
                ] + [
                    ((x, y), z)
                    for x in [4, -1]
                    for y in [0, -5]
                    for z in [0, -5]
                ]
            }
        )

        self.frame_4_0_4 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [4, 0, 4]],
            {
                'tuple': [
                    (x, y, z)
                    for x in [4, -1]
                    for y in [0, -5]
                    for z in [4, -1]
                ] + [
                    (x, (y, z))
                    for x in [4, -1]
                    for y in [0, -5]
                    for z in [4, -1]
                ] + [
                    ((x, y), z)
                    for x in [4, -1]
                    for y in [0, -5]
                    for z in [4, -1]
                ]
            }
        )

        self.frame_4_4_0 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [4, 4, 0]],
            {
                'tuple': [
                    (x, y, z)
                    for x in [4, -1]
                    for y in [4, -1]
                    for z in [0, -5]
                ] + [
                    (x, (y, z))
                    for x in [4, -1]
                    for y in [4, -1]
                    for z in [0, -5]
                ] + [
                    ((x, y), z)
                    for x in [4, -1]
                    for y in [4, -1]
                    for z in [0, -5]
                ]
            }
        )

        self.frame_0_0_0_4 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [0, 0, 0, 4]],
            {
                'tuple': [
                    ((w, x), (y, z))
                    for w in [0, -5]
                    for x in [0, -5]
                    for y in [0, -5]
                    for z in [4, -1]
                ],
            }
        )

        self.frame_0_0_4_0 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [0, 0, 4, 0]],
            {
                'tuple': [
                    ((w, x), (y, z))
                    for w in [0, -5]
                    for x in [0, -5]
                    for y in [4, -1]
                    for z in [0, -5]
                ],
            }
        )

        self.frame_0_4_0_0 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [0, 4, 0, 0]],
            {
                'tuple': [
                    ((w, x), (y, z))
                    for w in [0, -5]
                    for x in [4, -1]
                    for y in [0, -5]
                    for z in [0, -5]
                ],
            }
        )

        self.frame_0_4_0_4 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [0, 4, 0, 4]],
            {
                'tuple': [
                    ((w, x), (y, z))
                    for w in [0, -5]
                    for x in [4, -1]
                    for y in [0, -5]
                    for z in [4, -1]
                ],
            }
        )

        self.frame_0_4_4_0 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [0, 4, 4, 0]],
            {
                'tuple': [
                    ((w, x), (y, z))
                    for w in [0, -5]
                    for x in [4, -1]
                    for y in [4, -1]
                    for z in [0, -5]
                ],
            }
        )

        self.frame_4_0_0_0 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [4, 0, 0, 0]],
            {
                'tuple': [
                    ((w, x), (y, z))
                    for w in [4, -1]
                    for x in [0, -5]
                    for y in [0, -5]
                    for z in [0, -5]
                ],
            }
        )

        self.frame_4_0_0_4 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [4, 0, 0, 4]],
            {
                'tuple': [
                    ((w, x), (y, z))
                    for w in [4, -1]
                    for x in [0, -5]
                    for y in [0, -5]
                    for z in [4, -1]
                ],
            }
        )

        self.frame_4_0_4_0 = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [4, 0, 4, 0]],
            {
                'tuple': [
                    ((w, x), (y, z))
                    for w in [4, -1]
                    for x in [0, -5]
                    for y in [4, -1]
                    for z in [0, -5]
                ],
            }
        )

        self.every_2nd_frame = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [0, 2, 4]],
            {
                'abc': [
                    (None, None, 2),
                    (None, 100, 2),
                    (0, None, 2),
                    (0, 100, 2),
                    (-100, None, 2),
                    (-100, 100, 2),
                ]
            }
        )

        self.every_2nd_frame_rev = ExpectedResult(
            [video.segment(self.offset + i, 1) for i in [4, 2, 0]],
            {
                'abc': [
                    (100, -100, -2),
                    (-1, -100, -2),
                ]
            }
        )

        self.all_but_ends = ExpectedResult(
            [video.segment(self.offset + 1, 3)],
            {
                'ab': [
                    (1, -1),
                ],
                'abc': [
                    (1, -1, None),
                    (1, -1, 1),
                ]
            }
        )

        self.all_but_first = ExpectedResult(
            [video.segment(self.offset + 1, 4)],
            {
                'ab': [
                    (1, 100),
                    (1, None)
                ],
                'abc': [
                    (1, None, None),
                    (1, None, 1),
                    (1, 100, None),
                    (1, 100, 1),
                ]
            }
        )

        self.all_but_last = ExpectedResult(
            [video.segment(self.offset + 0, 4)],
            {
                'ab': [
                    (0, -1),
                    (-100, -1),
                    (None, -1),
                ],
                'abc': [
                    (None, -1, None),
                    (None, -1, 1),
                    (0, -1, None),
                    (0, -1, 1),
                    (-100, -1, None),
                    (-100, -1, 1),
                ]
            }
        )

        self.full_range = ExpectedResult(
            [video.segment(self.offset + 0, 5)],
            {
                'ab': [
                    (0, 100),
                    (-100, 100),
                    (0, None),
                    (-100, None),
                    (None, 100),
                    (None, None),
                ],
                'abc': [
                    (None, None, None),
                    (None, None, 1),
                    (None, 100, None),
                    (None, 100, 1),
                    (0, None, None),
                    (0, None, 1),
                    (0, 100, None),
                    (0, 100, 1),
                    (-100, None, None),
                    (-100, None, 1),
                    (-100, 100, None),
                    (-100, 100, 1),
                ]
            }
        )

        self.full_range_twice = ExpectedResult(
            [video.segment(self.offset + 0, 5),
             video.segment(self.offset + 0, 5)],
            {
                'tuple': {
                    (None, None),
                }
            }
        )

        self.frame_0_plus_full_range = ExpectedResult(
            [video.segment(self.offset + 0, 1),
             video.segment(self.offset + 0, 5)],
            {
                'tuple': {
                    (0, None),
                    (-5, None),
                }
            }
        )

        self.frame_1_plus_full_range = ExpectedResult(
            [video.segment(self.offset + 1, 1),
             video.segment(self.offset + 0, 5)],
            {
                'tuple': {
                    (1, None),
                }
            }
        )

        self.frame_4_plus_full_range = ExpectedResult(
            [video.segment(self.offset + 4, 1),
             video.segment(self.offset + 0, 5)],
            {
                'tuple': {
                    (4, None),
                    (-1, None),
                }
            }
        )

        self.full_range_plus_frame_0 = ExpectedResult(
            [video.segment(self.offset + 0, 5),
             video.segment(self.offset + 0, 1)],
            {
                'tuple': {
                    (None, 0),
                    (None, -5),
                }
            }
        )

        self.full_range_plus_frame_1 = ExpectedResult(
            [video.segment(self.offset + 0, 5),
             video.segment(self.offset + 1, 1)],
            {
                'tuple': {
                    (None, 1),
                }
            }
        )

        self.full_range_plus_frame_4 = ExpectedResult(
            [video.segment(self.offset + 0, 5),
             video.segment(self.offset + 4, 1)],
            {
                'tuple': {
                    (None, 4),
                    (None, -1),
                }
            }
        )

        self.non_empty = {
            'a': {
                **self.frame_0.non_empty['a'],
                **self.frame_4.non_empty['a'],
            },
            'ab': {
                **self.frame_0.non_empty['ab'],
                **self.frame_4.non_empty['ab'],
                **self.full_range.non_empty['ab'],
                **self.all_but_last.non_empty['ab'],
                **self.all_but_first.non_empty['ab'],
                **self.all_but_ends.non_empty['ab'],
            },
            'abc': {
                **self.frame_0.non_empty['abc'],
                **self.frame_1.non_empty['abc'],
                **self.frame_4.non_empty['abc'],
                **self.frame_0_2.non_empty['abc'],
                **self.frame_1_0.non_empty['abc'],
                **self.frame_1_3.non_empty['abc'],
                **self.frame_4_2.non_empty['abc'],
                **self.full_range.non_empty['abc'],
                **self.frame_4_to_0.non_empty['abc'],
                **self.frame_4_to_1.non_empty['abc'],
                **self.frame_4_to_2.non_empty['abc'],
                **self.all_but_last.non_empty['abc'],
                **self.all_but_first.non_empty['abc'],
                **self.all_but_ends.non_empty['abc'],
                **self.every_2nd_frame.non_empty['abc'],
                **self.every_2nd_frame_rev.non_empty['abc'],
            },
            'tuple': {
                **self.frame_0_1.non_empty['tuple'],
                **self.frame_0_4.non_empty['tuple'],
                **self.frame_0_twice.non_empty['tuple'],
                **self.frame_0_thrice.non_empty['tuple'],
                **self.frame_1_0.non_empty['tuple'],
                **self.frame_1_twice.non_empty['tuple'],
                **self.frame_1_4.non_empty['tuple'],
                **self.frame_4_0.non_empty['tuple'],
                **self.frame_4_1.non_empty['tuple'],
                **self.frame_4_twice.non_empty['tuple'],
                **self.frame_0_0_4.non_empty['tuple'],
                **self.frame_0_4_0.non_empty['tuple'],
                **self.frame_0_4_4.non_empty['tuple'],
                **self.frame_4_0_0.non_empty['tuple'],
                **self.frame_4_0_4.non_empty['tuple'],
                **self.frame_4_4_0.non_empty['tuple'],
                **self.frame_0_four_times.non_empty['tuple'],
                **self.frame_0_0_0_4.non_empty['tuple'],
                **self.frame_0_0_4_0.non_empty['tuple'],
                **self.frame_0_4_0_0.non_empty['tuple'],
                **self.frame_0_4_0_4.non_empty['tuple'],
                **self.frame_0_4_4_0.non_empty['tuple'],
                **self.frame_4_0_0_0.non_empty['tuple'],
                **self.frame_4_0_0_4.non_empty['tuple'],
                **self.frame_4_0_4_0.non_empty['tuple'],
                **self.full_range_twice.non_empty['tuple'],
                **self.full_range_plus_frame_0.non_empty['tuple'],
                **self.full_range_plus_frame_1.non_empty['tuple'],
                **self.full_range_plus_frame_4.non_empty['tuple'],
                **self.frame_0_plus_full_range.non_empty['tuple'],
                **self.frame_1_plus_full_range.non_empty['tuple'],
                **self.frame_4_plus_full_range.non_empty['tuple'],
            },
        }

indices = {
    'a': [0, 4, -1, -5, 5, -6],
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
        for x in [None, 0, 1, 4, -1, -5]
        for y in [None, 0, 1, 4, -1, -5]
    ] + [
        (x, y)
        for x in [0, 4, -1, -5, (0, 0), (0, -1), (0, 4), (4, -5)]
        for y in [0, 4, -1, -5, (0, 0), (0, -1), (0, 4), (4, -5)]
    ]
}

def at_the_beginning(video):
    #   Create a range of 5 frames at the beginning of the video
    video_range = (video, 0, 5)
    frame_range = mosher.FrameRange(*video_range)
    expected = Expected(*video_range)

    return (frame_range, indices, expected)

def in_the_middle(video):
    #   Create a single-frame frame range in the middle of the video
    video_range = (video, 10, 5)
    frame_range = mosher.FrameRange(*video_range)
    expected = Expected(*video_range)

    return (frame_range, indices, expected)

