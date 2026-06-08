filename = input("Enter file name: ")

with open(filename, "r") as file:
    text = file.read().lower()

words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("\nWord Frequencies:")
for word, count in word_count.items():
    print(word, ":", count)