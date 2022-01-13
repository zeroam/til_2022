from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    emp_id: str
    age: int
    city: str


if __name__ == "__main__":
    emp1 = Employee("Satyam", "ksatyam858", 21, "Patna")
    emp2 = Employee("Anurag", "au23", 28, "Delhi")
    emp3 = Employee("Satyam", "ksatyam858", 21, "Patna")

    print("Employee objecta are:")
    print(emp1)
    print(emp2)
    print(emp3)
    print()

    print("emp1 == emp2:", emp1 == emp2)
    print("emp1 == emp3:", emp1 == emp3)
    print()

    print(emp1.__dataclass_fields__)
