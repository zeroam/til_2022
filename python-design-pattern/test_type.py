class Point:
    def __init__(self, x, y):
        print("instantiate")
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


Point = type("Point", (), {"x": 1, "y": 2, "__repr__": lambda obj: f"Point ({obj.x}, {obj.y})"})
print(Point)

p = Point()
print(p)
