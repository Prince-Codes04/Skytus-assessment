class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

name = input("Enter Student Name: ")

marks = []
for i in range(5):
    mark = int(input(f"Enter Mark {i+1}: "))
    marks.append(mark)

student = Student(name, marks)

print("\nStudent Details")
print("Name:", student.name)
print("Marks:", student.marks)
print("Average Marks:", student.average())