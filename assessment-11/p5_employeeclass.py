class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("\nEmployee Details")
        print("Name :", self.name)
        print("Salary :", self.salary)

name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))

emp = Employee(name, salary)
emp.display()