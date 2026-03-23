#Task 1
numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    
    if user_input == "":
        break
    
    numbers.append(float(user_input))

numbers.sort(reverse=True)

print("Top 5 numbers:")
print(numbers[:5])

#Task 2
num = int(input("Enter an integer: "))

if num < 2:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

#Task 3
cities = []

for i in range(5):
    city = input(f"Enter city {i+1}: ")
    cities.append(city)

print("\nCities:")
for city in cities:
    print(city)

#Task 4
def sum_list(numbers):
    return sum(numbers)

# Main program
my_list = [1, 2, 3, 4, 5]
result = sum_list(my_list)

print("Sum of list:", result)

#Task 5
def remove_odd(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Main program
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = remove_odd(my_list)

print("Original list:", my_list)
print("Even numbers list:", new_list)