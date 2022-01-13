class Employee:
    def __init__(self, name, emp_id, age, city):
        self.name = name
        self.emp_id = emp_id
        self.age = age
        self.city = city

    def __repr__(self):
        return f"Employee(name={self.name}, emp_id={self.emp_id}, age={self.age}, city={self.age})"

    def __eq__(self, other: "Employee"):
        return (
            (self.name, self.emp_id, self.age, self.city) ==
            (other.name, other.emp_id, other.age, other.city)
        )


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
