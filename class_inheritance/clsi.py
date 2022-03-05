class First:
    def __init__(self):
        self.name = 'First'

    def get_name(self):
        return self.name

    @staticmethod
    def get_type():
        return 'Class'


class Second:
    def __init__(self):
        self.name = 'Second'

    def get_name(self):
        return self.name


class Third:
    def __init__(self):
        self.py = 'Python'

    def get_programming_language(self):
        return self.py


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
