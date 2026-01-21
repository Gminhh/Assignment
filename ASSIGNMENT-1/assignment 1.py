#Task 2
name = input("Your Name:")
print("Hello", name)

#Task 3
import math
radius = float(input("Radius of circle:"))
circumference = 2*math.pi*radius
print(f"circumference of the circle: {circumference:.2f}")

#Task 4
length = float(input("Length of rectangle:"))
width = float(input("Width of rectangle:"))
perimeter = (length+width)*2
area = length*width
print(f"perimeter of rectangle: {perimeter:.2f}")
print(f"area of rectangle: {area:.2f}")

#Task 5
integer1 = int(input("Integer 1:"))
integer2 = int(input("Integer 2:"))
integer3 = int(input("Integer 3:"))
sum = integer1 + integer2 + integer3
print("sum is:", sum)
product = integer1*integer2*integer3
print("product is:", product)
average = sum/3
print("average is:", average)

#Task 6
talents = float(input("Talents:"))
pounds = float(input("Pounds:"))
lot = float(input("Lot:"))
talents_to_gram = talents*20*32*13.3
pounds_to_gram = pounds*32*13.3
lot_to_gram = lot*13.3
total_gram = talents_to_gram + pounds_to_gram + lot_to_gram
kilograms = int(total_gram / 1000)
grams = float(total_gram - kilograms*1000)
print(f"kilograms: {kilograms} and grams: {grams:.2f}")

#Task 7
import random
a1 = random.randint(0,9)
a2 = random.randint(0,9)
a3 = random.randint(0,9)
print(f"combination lock of 3-digit code: {a1, a2, a3}")
b1 = random.randint(1,6)
b2 = random.randint(1,6)
b3 = random.randint(1,6)
b4 = random.randint(1,6)
print(f"combination lock of 4-digit code: {b1, b2, b3, b4}")

