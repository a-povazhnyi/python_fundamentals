# 1
def get_unique_keys(structure):
    used = []

    for dish in structure['Cook Book']:
        used.extend(*dish.values())
    return set(used)


# 2
def get_unique_keys_by_pop(structure):
    used = {}

    for dish in structure['Cook Book']:
        dish_values = list(*dish.values())

        for value in dish_values:
            if value not in used.keys():
                used[value] = 1
            else:
                used[value] += 1

    sorted_used = sorted(used, key=used.get, reverse=True)
    return sorted_used


# 3
class UniqueKeys:
    def __init__(self, structure, by_pop=False):
        self._structure = structure
        self._by_pop = by_pop
        self._current_index = -1

        if not self._by_pop:
            self._used = self.make_unique_keys()
            self._limit = len(self._used) - 1
        else:
            self._sorted_used = self.make_unique_keys_by_pop()
            self._limit = len(self._sorted_used) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self._current_index += 1

        if not self._by_pop:
            if self._current_index > self._limit:
                raise StopIteration
            else:
                return self._used[self._current_index]
        else:
            if self._current_index > self._limit:
                raise StopIteration
            else:
                return self._sorted_used[self._current_index]

    def make_unique_keys(self):
        used = []

        for dish in self._structure['Cook Book']:
            used.extend(*dish.values())
        return list(set(used))

    def make_unique_keys_by_pop(self):
        used = {}

        for dish in self._structure['Cook Book']:
            dish_values = list(*dish.values())

            for value in dish_values:
                if value not in used.keys():
                    used[value] = 1
                else:
                    used[value] += 1

        sorted_used = sorted(used, key=used.get, reverse=True)
        return sorted_used


cook_book = {
    "Cook Book": [
        {"Dish A": ["oil", "bacon", "oil"]},
        {"Dish B": ["eggs", "oil", "eggs"]}
    ]
}
