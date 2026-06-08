#-------1. Check if a person is eligible to vote (age ≥ 18)
print("Question 1:")

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


#------2. Grade calculator based on marks

print("Question 2:")

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")


#------3. Simulate a traffic light

print("Question 3:")

color = input("Enter traffic light color (Red/Yellow/Green): ")

if color.lower() == "red":
    print("Stop")
elif color.lower() == "yellow":
    print("Wait")
elif color.lower() == "green":
    print("Go")
else:
    print("Invalid color")



#------4. ATM withdrawal check

print("Question 4:")

balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if withdraw <= balance:
    print("Withdrawal successful")
    print("Remaining balance:", balance - withdraw)
else:
    print("Insufficient balance")



#------5. Check if a number is positive, negative, or zero

print("Question 5:")

num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


#------6. Check if a number lies within a given range

print("Question 6:")

num = int(input("Enter a number: "))
start = int(input("Enter range start: "))
end = int(input("Enter range end: "))

if start <= num <= end:
    print("Number is within the range")
else:
    print("Number is outside the range")    


#-----7. Username & password verification

print("Question 7:")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "PRINCE" and password == "P_R_I_N_C_E":
    print("Login successful")
else:
    print("Invalid username or password")


#------8. Electricity bill calculator based on units consumed

print("Question 8:")

units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
else:
    bill = units * 5

print("Electricity Bill =", bill)


#------9. Simple calculator (add, subtract, multiply, divide)

print("Question 9:")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result =", num1 + num2)
elif operation == "-":
    print("Result =", num1 - num2)
elif operation == "*":
    print("Result =", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid operation")


#-------10. Check type of triangle (equilateral, isosceles, scalene)

print("Question 10:")

side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")