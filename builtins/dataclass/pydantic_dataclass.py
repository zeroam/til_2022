from pydantic.dataclasses import dataclass


@dataclass
class Employee:
    name: str
    emp_id: str
    age: int
    city: str


jayone = Employee("jayone", "jcw", "invalid", "seoul")  # ValidationError 발생