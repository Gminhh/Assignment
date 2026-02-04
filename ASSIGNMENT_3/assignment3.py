#Task 1
num = 1
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1

#Task 2
INCH_TO_CM = 2.54
while True:
    inches = float(input("Enter inches (negative value to stop):"))
    if inches < 0:
        print("Program ends.")
        break
    centimeters = inches * INCH_TO_CM
    print(f"{inches} inches = {centimeters} centimeters")

#Task 3
numbers = []
while True:
    user_input = input(("Enter a number (Press ENTER to stop):"))
    if user_input == "":
        break
    numbers.append(float(user_input))
if numbers:
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
else:
    print("No number were entered") 

#Task 4
import random 
number = random.randint(1,10)
while True:
    guess = int(input("Guess a number between 1 and 10:"))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too Low")
    else:
        print("Correct!")
        break

#Task 5
correct_username = "python"
correct_password = "rules"
attempts = 0
max_attempts = 5
while attempts < max_attempts:
    username = input("Enter username:")
    password = input("Enter password:")
    
    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        attempts +=1
        print("Incorrect username or password!")
if attempts == max_attempts:
    print("Access denied")

#Task 6
def get_middle(user_input):
    length = len(user_input)
    middle = length // 2
    if length % 2 == 0:
        return user_input[middle - 1: middle +1]
    else:
        return user_input[middle]
user_input = input("Enter a string:")
result = get_middle(user_input)
print("Middle character(s):", result)

#Task 7
def make_acronym(phrase):
    words = phrase.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym
text = input("Enter a phrase:")
print("Acronym:", make_acronym(text))