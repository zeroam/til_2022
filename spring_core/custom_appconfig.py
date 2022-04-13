from abc import ABC, abstractmethod
from dataclasses import dataclass

repo = {}


@dataclass
class Member:
    id: int
    name: str


class MemberRepository(ABC):
    @abstractmethod
    def save(self, member: Member):
        ...

    @abstractmethod
    def find_by_id(self, id: int):
        ...


class MemoryMemberRepository(MemberRepository):
    def save(self, member: Member) -> None:
        repo[member.id] = member

    def find_by_id(self, id: int) -> Member:
        return repo[id]



class MemberService(ABC):
    @abstractmethod
    def join(self, member: Member):
        ...

    @abstractmethod
    def find_member(self, member_id: int) -> Member:
        ...


class MemberServiceImpl(MemberService):
    def __init__(self, member_repository: MemberRepository):
        self.member_repository = member_repository

    def join(self, member: Member):
        return self.member_repository.save(member)

    def find_member(self, member_id: int) -> Member:
        return self.member_repository.find_by_id(member_id)


class AppConfig:
    def get_service(self):
        return MemberServiceImpl(self.get_repository())

    def get_repository(self):
        return MemoryMemberRepository()


def main():
    app_config = AppConfig()

    member_service = app_config.get_service()
    member = Member(1, "jayone")
    member_service.join(member)

    find_member = member_service.find_member(1)

    print("new member =", member)
    print("find member =", find_member)


if __name__ == "__main__":
    main()
