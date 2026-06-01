age = int(input("Enter your age: "))
has_id = input("Do you have an ID (yes/no)? ")

if (age >= 18 and has_id == "yes") or age >= 60:
    print("Eligible")
else:
    print("Not Eligible")