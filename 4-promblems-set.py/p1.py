#################################################################
# Interview Question:
# Given two arrays, determine if both arrays contain exactly the 
# same elements in the same order.
#
# Difficulty: EASY
#################################################################

# Your variable table goes here!

# Variable : Value
# array1 : list([1, 2, 3, 4]) 
# array2 : list([1, 2, 7, 4])

def arrays_identical(array1, array2):
    # If arrays are different lengths, they are not identical.
    if len(array1) != len(array2):
        return False
    
    # Loop over each element to see if the items are equal.
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
  
    # If all items are equal, then arrays are identical.
    return True

actual = arrays_identical([1, 2, 3, 4], [1, 2, 7, 4])
expected = False

print(f"Testing on {[1, 2, 3, 4]}, {[1, 2, 7, 4]}")
if expected == actual:
  print("✅ Passed!")
else:
  print(f"❌ Failed! Expected {expected}, got {actual}")