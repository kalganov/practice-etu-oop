from house_animal import HouseAnimal


class Cow(HouseAnimal):
    what_does_the_cows_say = "МУУУУУ"

    def __init__(self, name, age):
        super().__init__(name)
        if age < 1:
            raise RuntimeError("Корова хочет иметь нормальный возраст")
        self.__age = age

    def say_something(self):
        return f"Меня зовут {self.name} и мне {self.__age} и я делаю {Cow.what_does_the_cows_say}"

    def get_age(self):
        return self.__age

    def set_age(self, new_age: int):
        if new_age < 1:
            raise RuntimeError("Корова хочет иметь нормальный возраст")
        self.__age = new_age

    def del_age(self):
        raise RuntimeError("Возраст - неотъемлимая часть коровы")

    age = property(get_age, set_age, del_age)
