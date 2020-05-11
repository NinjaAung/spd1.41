#################################################################
# Interview Question:
# Given a string containing a long text, find the most commonly 
# occurring word in the text as well as its count.
#
# Difficulty: MEDIUM
#################################################################


# Your variable table goes here!

# Variable : Value
# text : str('one fish two fish red fish blue fish')
# histogram : dict(word:freq)
# text_as_list : list([one, fish, two, fish, red, fish, blue, fish,])


def find_most_common_word(text):
    text_as_list = text.split(' ')
    histogram = {}

    # Make a dictionary of word -> count
    for word in text_as_list:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1

    # Find most common word
    most_common_word = text_as_list[0]
    for word in histogram:
        if histogram[word] > histogram[most_common_word]:
            most_common_word = word

    return (most_common_word, histogram[most_common_word])


expected = ('fish', 4)
actual = find_most_common_word('one fish two fish red fish blue fish')

print("Testing on 'one fish two fish red fish blue fish'")
if expected == actual:
  print("✅ Passed!")
else:
  print(f"❌ Failed! Expected {expected}, got {actual}")