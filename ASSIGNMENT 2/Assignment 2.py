# Task 1:
def fishing():
    size_limit =42
    length = float(input("Please enter the length of the zander (cm): "))
    if length < size_limit:
        difference = size_limit - length
        print('Release the fish back into the lake')
        print(f'The fish was {difference:.1f} cm below the size limit')
    else:
        print('The fish meets the size limit')

fishing()

#Task 2:

def cabin_class():
    cabin = input("Enter the cabin class (LUX, A, B, C): ").upper()
    if cabin == 'LUX':
        print('upper-deck cabin with a balcony.')
    elif cabin == 'A':
        print('above the car deck, equipped with a window.')
    elif cabin == 'B':
        print('windowless cabin above the car deck.')
    elif cabin == 'C':
        print('windowless cabin below the car deck.')
    else:
        print('Invalid cabin class')

cabin_class()

#Task 3:
#biological sex and hemoglobin value: BS_HV
def Sex():
    bio_sex = input("Enter biological sex (male/female): ").lower()
    hemo_value = float(input("Enter hemoglobin value (g/l): "))
    if bio_sex == 'female':
        if hemo_value < 117:
            print('the hemoglobin value is low,')
        elif hemo_value <= 155:
            print('the hemoglobin value is normal')
        else:
            print('the hemoglobin value is high')

    elif bio_sex == 'male':
        if hemo_value < 134:
            print('the hemoglobin value is low,')
        elif hemo_value <= 167:
            print('the hemoglobin value is normal,')
        else:
            print('the hemoglobin value is high,')

    else:
        print('Invalid hemoglobin value')

Sex()

#Task 4:

def Year():
    year = int(input("Please enter a year: "))
    if (year % 4 == 0 and year % 100) or (year % 400 == 0):
        print('This is a leap year')
    else:
        print('This is not a leap year')

Year()

#Task 5:

import math

def prices(diameter_cm, price):
    radius_m = (diameter_cm / 2) / 100  # convert cm to meters
    area = math.pi * radius_m ** 2
    return price / area


def pizzas():
    d1 = float(input("Enter diameter of pizza 1 (cm): "))
    p1 = float(input("Enter price of pizza 1 (USD): "))

    d2 = float(input("Enter diameter of pizza 2 (cm): "))
    p2 = float(input("Enter price of pizza 2 (USD): "))

    unit1 = prices(d1, p1)
    unit2 = prices(d2, p2)

    if unit1 < unit2:
        print("Pizza 1 provides better value for money.")
    elif unit2 < unit1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas have the same value for money.")

pizzas()