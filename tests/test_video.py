import mosher

import pytest

def mock_ffprobe_entry(entry):
    mock_entries = {
        'frame_count': 123,
        'frame_duration_s': 1.0/25.0,
    }
    return mock_entries[entry]

def test_video_properties():
    video = mosher.Video(42, 'mosh.avi')
    video._ffprobe_entry = mock_ffprobe_entry

    assert video.frame_count == 123
    assert video.frame_duration_s == 1.0/25.0
    assert video.frame_duration_us == video.frame_duration_s * 10**6

def test_segment():
    video = mosher.Video(42, 'mosh.avi')
    video._ffprobe_entry = mock_ffprobe_entry

    seg_10_1 = video.segment(10, 1)
    assert seg_10_1 == {
        'video_idx': 42,
        'video_start_frame': 10,
        'video_frame_count': 1,
        'start_us': 10 * video.frame_duration_us,
        'duration_us': 1 * video.frame_duration_us,
    }

def test_frames():
    video = mosher.Video(42, 'mosh.avi')
    video._ffprobe_entry = mock_ffprobe_entry

    assert list(video.I) == [{
        'video_idx': 42,
        'video_start_frame': 0,
        'video_frame_count': 1,
        'start_us': 0,
        'duration_us': 1 * video.frame_duration_us,
    }]

    assert list(video.P[0]) == [{
        'video_idx': 42,
        'video_start_frame': 1,
        'video_frame_count': 1,
        'start_us': 1 * video.frame_duration_us,
        'duration_us': 1 * video.frame_duration_us,
    }]

    assert list(video.P[10]) == [{
        'video_idx': 42,
        'video_start_frame': 11,
        'video_frame_count': 1,
        'start_us': 11 * video.frame_duration_us,
        'duration_us': 1 * video.frame_duration_us,
    }]

    assert list(video.P[1,0]) == [{
        'video_idx': 42,
        'video_start_frame': 2,
        'video_frame_count': 1,
        'start_us': 2 * video.frame_duration_us,
        'duration_us': 1 * video.frame_duration_us,
    }, {
        'video_idx': 42,
        'video_start_frame': 1,
        'video_frame_count': 1,
        'start_us': 1 * video.frame_duration_us,
        'duration_us': 1 * video.frame_duration_us,
    }]

