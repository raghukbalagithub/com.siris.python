"""
script to demo simple function in python
"""
expenses_p1 = [30, 140, 50]
expenses_p2 = [30, 410, 50]

def find_total_expenses(expenses):
    '''
    :param expenses: input list of expenses
    :return: total expenses
    '''
    total_expenses = 0
    for expense in expenses:
        total_expenses += expense
    return total_expenses

print("p1 expenses: ", find_total_expenses(expenses_p1))
print("p2 expenses: ", find_total_expenses(expenses_p2))

#how to print the documentation
help(find_total_expenses)