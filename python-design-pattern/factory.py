from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Mewo!!")


# 팩토리 클래스
class ForestFactory:
    def make_sound(self, object_type: str):
        return eval(object_type)().do_say()


if __name__ == "__main__":
    # 클라이언트 코드
    ff = ForestFactory()

    animal = "Dog"
    ff.make_sound(animal)

    animal = "Cat"
    ff.make_sound(animal)
