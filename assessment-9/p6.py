filename = input("Enter file name: ")
search_word = input("Enter word to search: ")

with open(filename, "r") as file:
    for line in file:
        if search_word.lower() in line.lower():
            print(line.strip())
            