#------1. Create a dictionary storing student names and marks.

# Creating a dictionary of student names and marks

students = {
    "Prince": 95,
    "Riyank": 92,
    "Priyal": 88,
    "Mahek": 98
}

print("Student Dictionary:")
print(students)


#------2. Add a new key-value pair to an existing dictionary.

student = {
    "Prince": 95,
    "Riyank": 92,
    "Priyal": 88,
    "Mahek": 98
}

name = input("Enter new student name: ")
marks = int(input("Enter marks: "))

student[name] = marks

print("Updated Dictionary:")
print(student)


#------ 3. Delete a key-value pair from a dictionary

student = {
    "Prince": 95,
    "Riyank": 92,
    "Priyal": 88,
    "Mahek": 98
}

key = input("Enter key to delete: ")

if key in student:
    del student[key]
    print("Key deleted successfully.")
else:
    print("Key not found.")

print(student)


#-------4. Merge two dictionaries into one
dict1 = {
    "A": 10,
    "B": 20
}

dict2 = {
    "C": 30,
    "D": 40
}

merged_dict = dict1 | dict2

print("Merged Dictionary:")
print(merged_dict)


#-------5. Check if a key exists in a dictionary

student = {
    "Prince": 95,
    "Riyank": 92,
    "Priyal": 88,
    "Mahek": 98
}

key = input("Enter key to search: ")

if key in student:
    print("Key exists.")
else:
    print("Key does not exist.")


#------6. Count word frequency in a given string using a dictionary    

text = input("Enter a sentence: ")

words = text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word Frequency:")
print(frequency)


#-------7. Find the key with the maximum value in a dictionary

student = {
     "Prince": 95,
    "Riyank": 92,
    "Priyal": 88,
    "Mahek": 98
}

max_key = max(student, key=student.get)

print("Key with maximum value:", max_key)
print("Maximum value:", student[max_key])

#------8. Reverse keys and values in a dictionary

student = {
    "Prince": 95,
    "Riyank": 92,
    "Priyal": 88,
    "Mahek": 98
}

reversed_dict = {}

for key, value in student.items():
    reversed_dict[value] = key

print("Reversed Dictionary:")
print(reversed_dict)


#------9. Update the value for a specific key

student = {
    "Prince": 95,
    "Riyank": 92,
    "Priyal": 88,
    "Mahek": 98
}

key = input("Enter key to update: ")

if key in student:
    new_value = int(input("Enter new value: "))
    student[key] = new_value
    print("Value updated successfully.")
else:
    print("Key not found.")

print(student)


#------10. Convert a list of tuples into a dictionary

# Convert a list of tuples into a dictionary

tuple_list = [
    ("Prince", 95),
    ("Riyank", 92),
    ("Priyal", 88),
    ("Mahek", 98)
]

student_dict = dict(tuple_list)

print("Dictionary:")
print(student_dict)