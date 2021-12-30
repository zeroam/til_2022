class Person(object):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<Person ({self.name})>"

    def __str__(self):
        return f"<Person name: {self.name}>"


if __name__ == "__main__":
    jayone = Person("jayone")
    print(repr(jayone))
    print(jayone)
    print(str(jayone))
