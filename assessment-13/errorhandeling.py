# ==============================
# 1. Handle Division by Zero Error
# ==============================

print("\n1. Division by Zero Error")

try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    print("Result =", num / den)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid integers.")


# ==============================
# 2. Handle Invalid Integer Input
# ==============================

print("\n2. Invalid Integer Input")

try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)

except ValueError:
    print("Error: Please enter a valid integer.")


# ==============================
# 3. Handle File Not Found Error
# ==============================

print("\n3. File Not Found")

try:
    filename = input("Enter file name: ")
    file = open(filename, "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: File not found.")


# ==============================
# 4. Multiple Exception Blocks
# ==============================

print("\n4. Multiple Exception Blocks")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Result =", num1 / num2)

except ValueError:
    print("Error: Invalid number entered.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as e:
    print("Unexpected Error:", e)


# ==============================
# 5. finally for Resource Cleanup
# ==============================

print("\n5. finally Example")

filename = input("Enter file name: ")

try:
    file = open(filename, "r")
    print(file.read())

except FileNotFoundError:
    print("Error: File not found.")

finally:
    try:
        file.close()
        print("File closed successfully.")
    except:
        print("No file to close.")


# ==============================
# 6. Custom Exception for Invalid Age
# ==============================

print("\n6. Custom Exception")

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("You are eligible.")

except InvalidAgeError as e:
    print("Error:", e)

except ValueError:
    print("Error: Enter a valid age.")


# ==============================
# 7. Handle IndexError
# ==============================

print("\n7. IndexError Example")

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index (0-4): "))
    print("Element =", numbers[index])

except IndexError:
    print("Error: Index out of range.")

except ValueError:
    print("Error: Enter a valid index.")


# ==============================
# 8. Handle All Possible Errors
# ==============================

print("\n8. Handle All Possible Errors")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Result =", num1 / num2)

except ValueError:
    print("Error: Invalid integer.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except Exception as e:
    print("Unexpected Error:", e)


# ==============================
# 9. Log Errors to a File
# ==============================

print("\n9. Log Errors to File")

try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))

    print("Result =", num / den)

except Exception as e:
    log = open("error_log.txt", "a")
    log.write(str(e) + "\n")
    log.close()

    print("Error logged in error_log.txt")


# ==============================
# 10. Validate Email Format
# ==============================

print("\n10. Email Validation")

class InvalidEmailError(Exception):
    pass

try:
    email = input("Enter your email: ")

    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email format.")

    print("Valid Email")

except InvalidEmailError as e:
    print("Error:", e)