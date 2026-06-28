score = 0

print("===== QUIZ GAME =====")

answer = input("1. What is the capital of India? ")
if answer.lower() == "delhi":
    score += 1

answer = input("2. 5 + 7 = ")
if answer == "12":
    score += 1

answer = input("3. Python was created by? ")
if answer.lower() == "guido van rossum":
    score += 1

answer = input("4. Full form of CPU? ")
if answer.lower() == "central processing unit":
    score += 1

answer = input("5. Which keyword is used for loops? ")
if answer.lower() == "for":
    score += 1

print("\nYour Score =", score, "/5")