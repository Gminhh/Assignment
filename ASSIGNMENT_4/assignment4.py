#Task 1
def Uni_codes(a):
    if len(a) != 6:         
        return False

    for i in range(3):              
        if not a[i].isupper():
            return False

    for i in range(3, 6):           
        if not a[i].isdigit():
            return False

    return True

a = input("Enter your university course code (3 uppercase letters and 3 digit numbers): ")

if Uni_codes(a):        
    print('Valid university code.')
else:
    print('Invalid university code.')

#Task 2
def Web_colors(b):
    if len(b) != 7:
        return False

    if b[0] != '#':
        return False

    for character in b[1:]:
        if not (character.isdigit() or character.lower() in "abcdef"):
            return False

    return True

b = input("Enter a hex color: ")
if Web_colors(b):
    print('Valid hex color.')
else:
    print('Invalid hex color.')

#Task 3:
text = "Today is January 16, 2025. The temperature is 11 degrees."
print(text)

def Sum_of_numbers(text):
    total = 0
    numbers = ""
    for k in text:
        if k.isdigit():
            numbers += k       
        else:
            if numbers != "":
                total += int(numbers)
                numbers = ""

    if numbers != "":               
        total += int(numbers)
    return total

print('The sum of all numbers found in text: ', Sum_of_numbers(text))

# Task 4
def hide_phone_numbers(phone):
    result = ""
    numbers = ""

    for i in phone:
        if i.isdigit() or i == '+':
            numbers += i
        else:
            if numbers != "":
                if numbers.isdigit() and len(numbers) == 10:                    
                    result += "[REDACTED]"
                elif numbers.startswith("+84") and numbers[1:].isdigit():       
                    result += "[REDACTED]"
                else:
                    result += numbers
                numbers = ""

            result += i

    if numbers != "":
        if numbers.isdigit() and len(numbers) == 10:
            result += "[REDACTED]"
        elif numbers.startswith("+84") and numbers[1:].isdigit():
            result += "[REDACTED]"
        else:
            result += numbers

    return result


phone = input("Enter text that contain phone numbers inside: ")
output = hide_phone_numbers(phone)
print("Result:", output)