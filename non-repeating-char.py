'''
Promblem: 
implement a function that takes a string and returns a character that only appears once. 
  Return the first unique character in the string. If there is no unique item retrun None.

Clarifying Questions: 
  Does the function only take a single word? Will it only be alpha or ascii(!{}<>,.) in general?

Assumptions: 
  The inputs are strings only, and it is only unique alpha characters will be returned

Possible Solutions: 

Simple: loop over the entire string AND pop the string 
  A hashtable that stores the values and a list that keeps track of all unique characters

'''



def non_repeating(string):
  dic = {}
  for index in range(0,len(string)):
    if string[index] in dic:
      del dic[string[index]]
    else:
      dic[string[index]] = 1
    
  if len(dic) == 0:
    return None

  return dic