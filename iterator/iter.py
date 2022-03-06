class Iterator:
    def __init__(self, sample: str):
        self._sample = sample
        self._limit = len(sample) - 1
        self._current_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self._current_index += 1

        if self._current_index > self._limit:
            raise StopIteration
        else:
            return self._sample[self._current_index]
