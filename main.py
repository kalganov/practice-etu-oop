class Cow:

    def __init__(self, name):
        self.name = name

    def say_something(self):
        return f"{self.name} делает МУУУУУУУУ"


if __name__ == '__main__':
    my_cow = Cow("мурка")
    print(my_cow.say_something())
