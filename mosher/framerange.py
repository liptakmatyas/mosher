class FrameRange:

    def __init__(self, video, video_start_frame, frame_count):
        """Constructor

        Parameters:
            video (Video)               Video object with the underlying data
            video_start_frame (int)     index of start frame in underlying video
            frame_count (int)           number of frames in the range
        """

        self._video = video
        self._offset = video_start_frame
        self._len = frame_count

    @property
    def video(self):
        return self._video

    def __iter__(self):
        yield self._video.segment(self._offset, self._len)

    def at(self, key):
        #   Make sure the index is in range
        if key < -self._len or key >= self._len:
            raise IndexError("frame index out of range: {}".format(key))

        #   Turn negative index into the positive one now that we know it's in
        #   the valid range
        if key < 0:
            key += self._len

        return self._video.segment(key + self._offset, 1)

    def slice(self, start = None, stop = None, step = None):
        #   No start means "from the beginning"
        #   No stop means "until the end"
        #   No step size means a step size of 1
        if start is None:
            start = 0
        if stop is None:
            stop = self._len
        if step == None:
            step = 1

        if step == 1:
            #   If the frames are consecutive, then produce a single
            #   segment, unless the frame count is zero

            if start < 0:
                start += self._len
            if start < 0:
                start = 0

            if stop < 0:
                stop += self._len
            if stop < 0:
                stop = 0

            frame_count = stop - start
            frame_count = min(frame_count, self._len - start)
            if frame_count > 0:
                yield self._video.segment(start + self._offset, frame_count)
        else:
            #   If the frames are not consecutive, then produce individual
            #   segments for them

            #   These checks are applicable to both directions
            if start < 0 and start >= -self._len:
                start += self._len
            if stop < 0:
                stop += self._len

            #   Different checks & corrections based on the direction
            if step < 0:
                if start >= self._len:
                    start = self._len - 1

            for frame_idx in range(start, stop, step):
                if frame_idx < 0 or frame_idx >= self._len:
                    continue
                yield self._video.segment(frame_idx + self._offset, 1)

    def __getitem__(self, key):
        if key is None:
            yield from self.slice(0, self._len, 1)
        elif type(key) == int:
            yield self.at(key)
        elif type(key) == slice:
            yield from self.slice(key.start, key.stop, key.step)
        elif type(key) == tuple:
            for k in key:
                yield from self.__getitem__(k)
        else:
            raise TypeError(type(key))

