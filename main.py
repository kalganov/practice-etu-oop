class Cow:

    what_does_the_cows_say = "МУУУУУ"

    def __init__(self, name):
        self.name = name

    def say_something(self):
        return f"{self.name} делает {Cow.what_does_the_cows_say}"


if __name__ == '__main__':
    my_cow = Cow("мурка")
    print(my_cow.say_something())
