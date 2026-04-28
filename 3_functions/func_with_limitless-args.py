"""
script to demonstrate functions with limitless arguments
"""

def sum_all_args(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print("sum of all the args: ", sum_all_args(1,2,3,4,5,6,7,8,9))