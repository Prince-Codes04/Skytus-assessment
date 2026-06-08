#------1. Print numbers from 1 to 10

print("Question 1:")

n = int(input("Enter the value of N: "))

for i in range(1, n + 1):
    print(i)



#------2. Display multiplication table for a given number


print("Question 2:")

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")   


#------3. Find factorial of a number


print("Question 3:")

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial =", factorial)


#------4. Generate the first N Fibonacci numbers

print("Question 4:")

n = int(input("Enter the value of N: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


#------5. Check if a number is prime


print("Question 5:")

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Not a Prime Number")


#------6. Reverse a number    

print("Question 6:")

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed Number =", reverse)


#------7. Count digits in a number

print("Question 7:")

num = int(input("Enter a number: "))
count = 0

while num > 0:
    count += 1
    num //= 10

print("Number of digits =", count)


#------8. Find sum of even numbers between 1–100

print("Question 8: Find sum of even numbers between 1 and N")

n = int(input("Enter the value of N: "))

sum_even = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i

print("Sum of even numbers =", sum_even)


#------9. Print a pyramid pattern


print("Question 9:")

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))



#-------10. Find all divisors of a number


print("Question 10:")

num = int(input("Enter a number: "))

print("Divisors are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)