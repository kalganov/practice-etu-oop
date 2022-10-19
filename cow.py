class Cow:
    what_does_the_cows_say = "МУУУУУ"

    def __init__(self, name, age):
        if age < 1:
            raise RuntimeError("Корова хочет иметь нормальный возраст")
        self.__name = name
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

    def get_name(self):
        return self.__name

    def set_name(self, new_age):
        raise RuntimeError("Корове дают имя при рождении")

    def del_name(self):
        raise RuntimeError("Имя - неотъемлимая часть коровы")

    age = property(get_age, set_age, del_age)
    name = property(get_name, set_name, del_name)
