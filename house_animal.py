class HouseAnimal:

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, new_age):
        raise RuntimeError("Домашнему животному дают имя при рождении")

    def del_name(self):
        raise RuntimeError("Имя - неотъемлимая часть домашнего животного")

    name = property(get_name, set_name, del_name)