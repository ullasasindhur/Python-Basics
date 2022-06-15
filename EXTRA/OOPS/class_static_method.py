from tokenize import Number
from xmlrpc.client import Boolean


class A:
    def __init__(self, age) -> None:
        self.age = age

    @classmethod
    def age_from_year(cls, year):
        return cls(2022 - year)

    @staticmethod
    def is_adult(age) -> Boolean:
        return True if age > 18 else False

    def get_age(self):
        print(self.age)


if __name__ == "__main__":
    obj = A(5)
    obj.get_age()
    obj1 = A.age_from_year(2000)
    obj1.get_age()
    print(A.is_adult(55))
    print(A.is_adult(8))
