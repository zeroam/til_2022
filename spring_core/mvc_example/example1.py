from dataclasses import dataclass
import json


repo = {}


@dataclass
class User:
    id: int
    name: str
    city: str

    def __iter__(self):
        yield from {
            "id": self.id,
            "name": self.name,
            "city": self.city
        }.items()


class Repository:
    def __init__(self):
        self.class_name = self.__class__.__name__

    def save(self, user: User) -> None:
        print(f"[{self.class_name}] add user: {user}")
        repo[user.id] = user

    def find_by_id(self, id: int) -> User:
        print(f"[{self.class_name}] get user: {id}")
        return repo[id]


class Service:
    repository: Repository = Repository()

    def __init__(self):
        self.class_name = self.__class__.__name__

    def logic(self):
        print(f"[{self.class_name}] execute business logic")

        self.repository.save(User(id=1, name="jayone", city="seoul"))
        user = self.repository.find_by_id(1)

        return dict(user)


class Controller:
    service: Service = Service()

    def __init__(self):
        self.class_name = self.__class__.__name__

    def get_index(self):
        print(f"[{self.class_name}] get web request")
        return json.dumps(self.service.logic())


class WebServer:
    def __init__(self):
        self._routes = {}

    def add_controller(self, controller):
        self._routes[controller.__class__.__name__] = controller

    def run(self):
        print("run server...")

    def request(self, class_name: str, func_name: str):
        controller = self._routes[class_name]
        func = getattr(controller, func_name)
        return func()


def main():
    controller = Controller()

    server = WebServer()
    server.add_controller(controller)

    # run server
    server.run()

    # request example
    print("[web] request start")
    print("[web]" + server.request("Controller", "get_index"))
    print("[web] request end")


if __name__ == "__main__":
    main()
