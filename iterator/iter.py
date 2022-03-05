class Iterator:
    def __init__(self, sample):
        self.sample = sample
        self.limit = len(sample)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.sample[self.counter - 1]
        raise StopIteration
