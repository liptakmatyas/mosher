import mosher

from mosher_testlib.mock import DummyVideo
from mosher_testlib.scenarios import (
    single_frame_range,
    multi_frame_range,
)

import pytest


_scenarios = [
    single_frame_range.at_the_beginning,
    single_frame_range.in_the_middle,
    multi_frame_range.at_the_beginning,
    multi_frame_range.in_the_middle,
]

@pytest.mark.parametrize("test_data", _scenarios)
def test_no_indexing(test_data):
    mock_video = DummyVideo(idx = 42, input_file = 'mock.avi', fps = 25)
    frame_range, indices, expected = test_data(mock_video)

    #   Without indexing or slicing, it should iterate into one segment
    #   representing the whole frame range.
    assert list(frame_range) == expected.full_range.segment_list
    assert list(frame_range[None]) == expected.full_range.segment_list

@pytest.mark.parametrize("test_data", _scenarios)
def test_integer_indexing(test_data):
    mock_video = DummyVideo(idx = 42, input_file = 'mock.avi', fps = 25)
    (frame_range, indices, expected) = test_data(mock_video)

    (indices, non_empty) = (indices['a'], expected.non_empty['a'])

    for i in indices:
        exp_segment = non_empty.get(i)
        print("[test_integer_indexing]", i, exp_segment)
        if exp_segment is not None:
            assert list(frame_range[i]) == exp_segment
        else:
            with pytest.raises(IndexError):
                list(frame_range[i])

@pytest.mark.parametrize("test_data", _scenarios)
def test_ab_slicing(test_data):
    mock_video = DummyVideo(idx = 42, input_file = 'mock.avi', fps = 25)
    frame_range, indices, expected = test_data(mock_video)

    (indices, non_empty) = (indices['ab'], expected.non_empty['ab'])

    for a in indices['a']:
        for b in indices['b']:
            exp_segment = non_empty.get((a, b), [])
            print("[test_ab_slicing]", a, b, exp_segment)
            assert list(frame_range[a:b]) == exp_segment

@pytest.mark.parametrize("test_data", _scenarios)
def test_abc_slicing(test_data):
    mock_video = DummyVideo(idx = 42, input_file = 'mock.avi', fps = 25)
    frame_range, indices, expected = test_data(mock_video)

    (indices, non_empty) = (indices['abc'], expected.non_empty['abc'])

    for a in indices['a']:
        for b in indices['b']:
            for c in indices['c']:
                if c != 0:
                    exp_segment = non_empty.get((a, b, c), [])
                    print("[test_ab_slicing]", a, b, c, exp_segment)
                    assert list(frame_range[a:b:c]) == exp_segment
                else:
                    #   Slice step size cannot be zero
                    with pytest.raises(ValueError):
                        list(frame_range[a:b:0])

@pytest.mark.parametrize("test_data", _scenarios)
def test_tuple_indexing(test_data):
    mock_video = DummyVideo(idx = 42, input_file = 'mock.avi', fps = 25)
    (frame_range, indices, expected) = test_data(mock_video)

    (indices, non_empty) = (indices['tuple'], expected.non_empty['tuple'])

    for i in indices:
        exp_segment = non_empty.get(i, [])
        print("[test_tuple_indexing]", i, exp_segment)
        assert list(frame_range[i]) == exp_segment

