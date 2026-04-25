"""
script to  practice if..else, if..elif..else in python
"""

print("Provide a number to find if it is negative, positive or a zero")
number = int(input("enter a number: "))
if number < 0:
    print("negative number")
elif number > 0:
    print("positive number")
else:
    print("zero number")

print("Next is to find if the given number is even or odd")
number = int(input("enter a number: "))
if number % 2 == 0:
    print(f"{number} - even number")
else:
    print(f"{number} - odd number")

print("Next, use the negative sense of condition")
number = int(input("enter a number: "))
if not number % 2 == 0:
    print(f"{number} - odd number")
else:
    print(f"{number} - even number")