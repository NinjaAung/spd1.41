# Given a non-negative integer num, return the number of steps to reduce it to zero. 
# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

# Variable Table
#  Variable  |  Value
# ____________________
#  Num        | 5 -> 4 -> 2 -> 1 -> 0
#  Steps      | 0 -> 1 -> 2 -> 3 -> 4

def num_step_counter(num):
    """Given a number, count the number of steps it will take to reduce the number to 0.
        if number is even divide by 2, if number is odd subtract 1.
        Time Analysis:
            O(k), where k is the number of steps needed to take.
        args:
            num - int
        return:
            steps - int"""
    steps = 0
    while num != 0:
        if num & 1:
            num -= 1
        elif num & 1 == 0:
            num = num // 2
        steps += 1
    return steps
        

# Given an array of integers arr, write a function that returns true if and only if 
# the number of occurrences of each value in the array is unique.

# Variable Table
#   Variable  |  Value
# ________|___________
# Num_arr   | [1, 1, 2]
# num_dict   | {} -> {1:1} -> {1:2} -> {1:2, 2:1}
# num           | 1 -> 1 -> 2 // 2 -> 1
# num_set    | {} -> {2} -> {2, 1}
def uniqueOccurrences(num_arr):
    """Given an array of numbers, check if the number of occurances of each number is unique
        Time Complexity:
            O(n), where n is the size of the initial array.
        Space Complexity:
        O(n), where n is the size of the array.
        args:
            num_arr - array
        return:
            bool"""
    num_dict = dict()
    num_set = set()

    for num in num_arr:
        num_dict[num] = num_dict.get(num, 0) + 1

    for num in num_dict.values():
        if num in num_set:
            return False
        num_set.add(num)

    return True