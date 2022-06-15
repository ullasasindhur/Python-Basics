class A:
    def __init__(self, name):
        self.name = name
        print("A")

    def get_name(self):
        print(self.name)


class B(A):
    def __init__(self, name, age):
        print("B")
        self.age = age
        super().__init__(name)

    def get_age(self):
        print(self.age)


class C(B):
    def __init__(self, name, age, sex):
        self.sex = sex
        print("C")
        super().__init__(name, age)

    def get_sex(self):
        print(self.sex)


if __name__ == "__main__":
    obj = C("poojith", 22, "M")
    obj.get_age()
    obj.get_name()
    obj.get_age()
