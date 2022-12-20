class Animal:
    def __init__(self, name):
        print("Animal Create")
        self.username = name

    def Say(self):
        pass


class Wise:
    def __init__(self):
        print("Wise Create")
        self.language = "Wise"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Cat Create")

    def Say(self):
        print("miao miao miao")


class People(Animal, Wise):
    def __init__(self):
        Wise.__init__(self)
        Animal.__init__(self, "People")
        # 使用super不能实现多继承
        # super(People, self).__init__("People")
        print("People Create")


if __name__ == '__main__':
    cat = Cat("name")
    cat.Say()
    print(isinstance(cat, Animal))
    print(isinstance(cat, Cat))

    people = People()