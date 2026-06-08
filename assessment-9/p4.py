filename = input("Enter file name: ")

with open(filename, "w") as file:
    for i in range(5):
        sentence = input(f"Enter sentence {i+1}: ")
        file.write(sentence + "\n")

print("Data written successfully.")