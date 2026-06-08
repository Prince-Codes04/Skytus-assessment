file_name = input("Enter file name: ")

with open(file_name, "w") as file:
    for i in range(5):
        sentence = input(f"Enter sentence {i+1}: ")
        file.write(sentence + "\n")

print("5 sentences written successfully.")