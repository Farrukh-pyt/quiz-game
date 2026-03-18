print("Welcome to the Quiz Game!")

score = 0

# Question 1
answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 2
answer = input("What is 5 + 7? ")
if answer == "12":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 3
answer = input("What programming language are we using? ")
if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nYour final score is:", score, "/ 3")
