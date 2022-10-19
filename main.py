# Функция
def create_cow():
    return Cow("мурка", 4)


class Cow:
    what_does_the_cows_say = "МУУУУУ"

    # Конструктор
    def __init__(self, name, age):
        # Публичное поле
        self.name = name
        # Конвенция по именованию приватных полей __var_name
        self.__age = age

    # Метод
    def say_something(self):
        return f"Меня зовут {self.name} и мне {self.__age} и я делаю {Cow.what_does_the_cows_say}"

    # В других ЯП - геттер
    def get_age(self):
        raise RuntimeError("Стыдно спрашивать такие вещи у коровы")

    # В других ЯП - сеттер
    def set_age(self, new_age):
        raise RuntimeError("Корова сама определит свой возраст!")

    # Личный прикол питона - можно добавлять классу поля, даже если он не очень хочет
    def del_age(self):
        raise RuntimeError("Возраст - неотъемлимая часть коровы")

    age = property(get_age, set_age, del_age)

    def say_something_wierd(self):
        return f"Меня зовут {self.name} {self.surname} и мне {self.__age} и я делаю {Cow.what_does_the_cows_say}"

    def happy_birthday(self):
        self.__age += 1


if __name__ == '__main__':
    my_cow = Cow("мурка", 4)
    # print(my_cow.__age)

    # Name mangling
    # print(my_cow._Cow__age)

    # my_cow.age = 123

    # print(my_cow.age)

    # print(my_cow.say_something())

    # my_cow.surname = "Ивановна"
    # print(my_cow.say_something_wierd())

    # del my_cow.surname
    # print(my_cow.say_something_wierd())
