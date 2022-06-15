from unicodedata import name


class A:
    def __init__(self, name):
        self.name = name

    def infoA(self):
        print("A", self.name)


class B(A):
    def __init__(self, age):
        super().__init__("poojith")
        self.age = age

    def infoB(self):
        print("B", self.age)


if __name__ == "__main__":
    obj = B(25)
    obj.infoA()
    obj.infoB()
