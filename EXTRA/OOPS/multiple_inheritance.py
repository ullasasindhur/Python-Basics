class A:
    def __init__(self, name):
        print("A")
        self.name = name

    def a(self):
        print("A is called", self.name)


class B:
    def __init__(self, age):
        print("B")
        self.age = age

    def b(self):
        print("B is called", self.age)


class C(B, A):
    def __init__(self, name, sex, age):
        print("C")
        super().__init__(age)
        self.sex = sex
        # self.name = name
        # super(A, self).__init__()
        A.__init__(self, name)

    def c(self):
        print("C is called", self.sex)


if __name__ == "__main__":
    obj = C("poojith", "F", 25)
    obj.c()
    obj.b()
    obj.a()
