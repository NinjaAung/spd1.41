'''
Given an array of integers arr, write a function that returns true if and only if 
the number of occurrences of each value in the array is unique.

variable : value
___________________________________________________________________________________________________________________________
num_arr : list, args input      | [1,        2,           5,                3,                   5, 6]
dic : dict, number:occurence    | {1:1} - > {1:1,2:1} -> {1:1,2:1,5:1} - > {1:1,2:1,5:1,3:1} -> {1:1,2:1,5:2,3:1} -> False
_________________________________________________________________________________
'''

def uniqueOccurrences(num_arr):
    """
    Given an array of numbers, check if the number of occurances of each number is unique
    _____________________________________________________________________________________________________________________________
    Time Complexity:                                 |  Space Complexity:                        |  args:           | return:
    O(n), where n is the size of the initial array.  |  O(n), where n is the size of the array.  |  num_arr - array | bool
    """
    dic = {}
    for num in num_arr:
        dic[num] = dic.get(num, 0) + 1
        if dic[num] > 1:
            return False
    return True