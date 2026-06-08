source_file = input("Enter source file name: ")
backup_file = input("Enter backup file name: ")

with open(source_file, "r") as source:
    content = source.read()

with open(backup_file, "w") as backup:
    backup.write(content)

print("Backup created successfully.")