class Foo:
    def __new__(cls, *args, **kwargs):
        print("new called")
        print(f"new {cls}, {args}, {kwargs}")
        obj = super().__new__(cls)
        print(f"new obj: {obj}")
        return obj

    def __init__(self, x, y):
        print("init called")
        self.x = x
        self.y = y


if __name__ == "__main__":
    foo = Foo(3, y=5)
