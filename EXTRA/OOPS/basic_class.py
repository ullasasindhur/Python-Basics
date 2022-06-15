class Car:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Hello")


if __name__ == "__main__":
    obj = Car("BMW")
    obj.info()
