#################################################################
# Interview Question:
# Given a string, find the longest substring containing all unique
# characters.
#
# Difficulty: HARD
#################################################################


class Histogram:
  """Helper class to store a histogram of letter -> count."""
  def __init__(self):
    self.dict = {}

  def add(self, value):
    """If value already exists, increase its count. Otherwise, add it."""
    if value in self.dict:
      self.dict[value] += 1
    else:
      self.dict[value] = 1

  def remove(self, value):
    """Decrease value's count. If count <= 0, remove it."""
    if value not in self.dict:
      return
    self.dict[value] -= 1
    if self.dict[value] <= 0:
      self.dict.pop(value)

  def contains(self, value):
    return value in self.dict

  def get(self, value):
    return self.dict[value]

  def __repr__(self):
      return str(self.dict)


# Your variable table goes here!

# Variable : Value
# str : str()
# chars_seen : Histogram()
# longest_unique_substring : str('bcaxyz')
# start : int(0)
# end : int(0)

def longest_unique_substring(str):
  # Define starting variables. 'start' and 'end' will determine which
  # substring we're currently looking at
  start = 0
  end = 0
  chars_seen = Histogram()
  
  longest_unique_substring = ''
  
  while end < len(str):
    if len(str[start:end]) > len(longest_unique_substring):
      longest_unique_substring = str[start:end]
      
    next_char = str[end]
    
    while chars_seen.contains(next_char):
      chars_seen.remove(str[start])
      start += 1
    
    chars_seen.add(next_char)
    end += 1

  print(chars_seen)
  return longest_unique_substring
  

expected = 'bcaxyz'
actual = longest_unique_substring('abcaxyz')

print("Testing on 'abcaxyz'")
if expected == actual:
  print("✅ Passed!")
else:
  print(f"❌ Failed! Expected {expected}, got {actual}")