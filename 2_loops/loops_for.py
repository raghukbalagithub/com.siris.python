"""
script to practice for loop and its types in python
"""

expenses = [1200, 1300, 900, 1700, 800]

print(f"number of expenses: {len(expenses)}")
total_expense = 0

#for loop - 1
print()
for expense in expenses:
    print(f"expense: {expense}")
    total_expense = total_expense + expense

print(f"total expense: {total_expense}\n")

#for loop - 2
print()
for i in range(len(expenses)):
    print(f"expense for month-{i+1}: {expenses[i]}")

#for loop - 3
print()
for i, expense in enumerate(expenses):
    print(f"expense for month-{i+1}: {expense}")

#for with break
print()
threshold = 1500
for expense in expenses:
    if expense > threshold:
        print(f"expense for month-{i+1}: {expense} higher than threshold: {threshold}")
        break
    else:
        print(f"expense for month-{i+1}: {expense} below threshold: {threshold}")

#for with zip
print()
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

for a_item, b_item in zip(a, b):
    print(f"{a_item}: {b_item}")

#for with continue - to print only odd numbers
print()
for i in range(1, 11):
    if i % 2 == 0:
        continue
    else:
        print(i)

print()
n = -5
message = "Negative" if n >= 0 else "Positive"
print(message)