class Test:
    def prt(self):
        print(self)
        print(self.__class__)


class Test1:
    def prt(jiyik):
        print(jiyik)
        print(jiyik.__class__)

if __name__ == '__main__':
    emp1 = Test()
    emp1.prt()
    emp1.age = 7  # Add an 'age' attribute.
    print(emp1.age)
    emp1.age = 8  # Modify 'age' attribute.
    print(emp1.age)
    del emp1.age  # Delete 'age' attribute.

    emp1.age = 19000

    print(hasattr(emp1, 'age'))  # Returns true if 'age' attribute exists
    print(getattr(emp1, 'age'))  # Returns value of 'age' attribute
    print(setattr(emp1, 'age', 8))  # Set attribute 'age' at 8
    print(delattr(emp1, 'age'))  # Delete attribute 'age'

    t1 = Test1()
    t1.prt()