from cow import Cow


class Herd:

    def __init__(self):
        self._cows = []

    def add_cow(self, new_cow: Cow):
        cows_name = map(Cow.get_name, self._cows)

        if new_cow.get_name() in cows_name:
            raise RuntimeError("Корова с таким именем уже есть в стаде")

        self._cows.append(new_cow)

    def cows_say_something(self):
        for cow in self._cows:
            print(cow.say_something())
