def simple_interest(p, r, t):
    return (p * r * t) / 100

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (years): "))

print("Simple Interest =", simple_interest(principal, rate, time))