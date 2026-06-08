filename = input("Enter file name: ")

n = int(input("How many strings do you want to append? "))

with open(filename, "a") as file:
    for i in range(n):
        text = input("Enter string: ")
        file.write(text + "\n")

print("Strings appended successfully.")