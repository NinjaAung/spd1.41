#################################################################
# Interview Question:
# Given a list of n numbers, find the highest pair of adjacent
# elements. That is, maximize a[i] + a[i+1] for some i.
#
# Difficulty: MEDIUM
#################################################################


# Your variable table goes here!

# Variable : Value
# the_list : list([7, 2, 5, 9, 3, 4])
# highest_pair : int([i] + [i+1])


def find_highest_pair(the_list):
  # Set it to lowest possible number
    highest_pair = float('-inf')
  
  # Loop over all indices in the list
    for i in range(len(the_list)):
        if i == len(the_list)-1:
            return highest_pair

        if highest_pair < the_list[i] + the_list[i+1]:
            highest_pair = the_list[i] + the_list[i+1]


actual = find_highest_pair([7, 2, 5, 9, 3, 4])
expected = 14

print(f"Testing on {[7, 2, 5, 9, 3, 4]}")
if expected == actual:
  print("✅ Passed!")
else:
  print(f"❌ Failed! Expected {expected}, got {actual}")