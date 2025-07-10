class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Employee(name='{self.name}', age={self.age}, salary={self.salary})"