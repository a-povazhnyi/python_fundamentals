class Iterator:
    def __init__(self, sample: str):
        self._sample = sample
        self._limit = len(sample) - 1
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index > self._limit:
            raise StopIteration

        result = self._sample[self._current_index]
        self._current_index += 1
        return result
