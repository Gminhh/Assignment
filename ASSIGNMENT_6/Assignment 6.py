# Task 1

numbers = []

while True:
    user_input = input("Enter a number (Enter nothing to quit): ")

    if user_input == "":
        break

    numbers.append(float(user_input))

numbers.sort(reverse=True)

print("Five greatest numbers:")
for i in range(min(5, len(numbers))):
    print(numbers[i])
print("")

# Task 2

seasons = ("winter", "spring", "summer", "autumn")

while True:
    month = int(input("Enter month number (1-12): "))
    if month == 12 or month == 1 or month == 2:
        print(seasons[0])
        break
    elif month >= 3 and month <= 5:
        print(seasons[1])
        break
    elif month >= 6 and month <= 8:
        print(seasons[2])
        break
    elif month >= 9 and month <= 11:
        print(seasons[3])
        break
    else:
        print("Invalid month number. Try again (1-12).")
print("")

# Task 3

names = set()

while True:
    name = input("Enter a name (Enter nothing to quit): ")

    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nNames entered:")
for n in names:
    print(n)
print("")

# Task 4

def word_frequency(text):
    words = text.split()
    freq = {}

    for word in words:
        word = word.lower()
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


text = input("Enter a text: ")

result = word_frequency(text)

for word, count in result.items():
    print(word, ":", count)
print("")


# Task 5

def remove_odds(numbers):
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


original = [1, 2, 3, 24, 56, 67, 90, 85, 99, 100]

result = remove_odds(original)

print("Original list:", original)
print("Cut-out odds number list: ", result)
print("")

# Task 6

import random

points = int(input("How many random points to generate: "))

inside_circle = 0
total_points = 0

for i in range(points):

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    total_points += 1

    if x**2 + y**2 < 1:
        inside_circle += 1

pi = 4 * inside_circle / total_points

print("Approximation of pi:", pi)