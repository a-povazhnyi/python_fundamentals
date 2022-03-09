from collections import Counter


# 1
def get_unique_keys(structure):
    used = []

    for dish in structure['Cook Book']:
        used.extend(*dish.values())
    return list(set(used))


# 2
def get_unique_keys_by_pop(structure):
    used = Counter()

    for dish in structure['Cook Book']:
        dish_values = list(*dish.values())

        for value in dish_values:
            used[value] += 1

    return list(used.keys())


# 3
class UniqueKeys:
    def __init__(self, structure, by_pop=False):
        self._structure = structure['Cook Book']
        self._by_pop = by_pop
        self._current_index = 0
        self._used = self.make_unique_keys(self._structure)

        if self._by_pop:
            self._used = self.make_unique_keys_by_pop(self._structure)

        self._limit = len(self._used) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index > self._limit:
            raise StopIteration

        result = self._used[self._current_index]
        self._current_index += 1
        return result

    @staticmethod
    def make_unique_keys(structure):
        used = []

        for dish in structure:
            used.extend(*dish.values())
        return list(set(used))

    @staticmethod
    def make_unique_keys_by_pop(structure):
        used = Counter()

        for dish in structure:
            dish_values = list(*dish.values())

            for value in dish_values:
                used[value] += 1

        return list(used.keys())


cook_book = {
    "Cook Book": [
        {"Dish A": ["oil", "bacon", "oil"]},
        {"Dish B": ["eggs", "oil", "eggs"]}
    ]
}
