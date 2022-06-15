from tokenize import Number, String


class Student:
    def __init__(self, name, id) -> None:
        self._name = name
        self.__id = id

    def get_name(self) -> String:
        return self._name

    def get_id(self) -> Number:
        return self.__id


class Parent(Student):
    def __init__(self, name, id, relation) -> None:
        super().__init__(name, id)
        self.relation = relation

    def print_self(self):
        print(self.relation, self._name)


if __name__ == "__main__":
    obj = Parent("poojith", 1505, "Father")
    obj.print_self()
    print(obj.get_id())
