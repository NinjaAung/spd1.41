'''
Given a non-negative integer num, return the number of steps to reduce it to zero. 
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

variable : value
___________________________________________________________________
current_num : int, currently                | 6 -> 3 -> 2 -> 1 -> 0
steps: returned int, of most recent step    | 0 -> 1 -> 2 -> 3 -> 4
'''

def num_step_counter(num):
    """
    Given a number, count the number of steps it will take to reduce the number to 0.
    if number is even divide by 2, if number is odd subtract 1.
    _________________________________________________________________________________
    Time Analysis:                                          |  args:      | return:
    O(k), where k is the number of steps needed to take.    |  num - int  | steps - int
    """
    steps = 0
    while num != 0:
        if num & 1:
            num -= 1
        elif num & 1 == 0:
            num = num // 2
        steps += 1
    return steps
