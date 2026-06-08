file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")
file3 = input("Enter output file name: ")

with open(file1, "r") as f1:
    content1 = f1.read()

with open(file2, "r") as f2:
    content2 = f2.read()

with open(file3, "w") as f3:
    f3.write(content1)
    f3.write("\n")
    f3.write(content2)

print("Files merged successfully.")