class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def display(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("Course :", self.course)

name = input("Enter Student Name: ")
course = input("Enter Course: ")

student = Student(name, course)

student.display()
