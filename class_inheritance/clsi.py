class First:
    def __init__(self):
        self._name = 'First'

    def get_name(self):
        return self._name

    @staticmethod
    def get_type():
        return 'Class'


class Second:
    def __init__(self):
        self._name = 'Second'

    def get_name(self):
        return self._name


class Third:
    def __init__(self):
        self._py = 'Python'

    def get_programming_language(self):
        return self._py


class Chest(First, Second, Third):
    def get_programming_language(self):
        return 'not Python'


chest = Chest()

chest.get_name()
# >>> 'First'

chest.get_programming_language()
# >>> 'not Python'

chest.get_type()
# with @staticmethod
# >>> 'Class'

# with @classmethod
# >>> 'Class'
