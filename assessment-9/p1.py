print("Question 1: Read a file and display its contents")

filename = input("Enter file name: ")

with open(filename, "r") as file:
    content = file.read()

print("\nFile Contents:")
print(content)