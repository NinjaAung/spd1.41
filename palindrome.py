'''
Problem: 
  Write a function to determine if a string is a palindrome or not

Clarifying Questions:
  will the string have all ascii character, if so will we have to match them as well? will we take in conserdeation of spaces as well? Will we return a bool? 

Assumptions: 
  The inputs are strings only, we will omit punctuation and spaces, returns a bool

Possible Solutions: 
  Python built ins allows a string slice with inverse that can compare the origonal string

  we check at each index from left to right starting at opposite ends and return False in any case they dont equal omititing spaces and non alphas

'''



def isPalindrome(text):
  return text == text[::-1] # built-ins: python


def palindrome(text):
  left = right = 0
  text = text.lower()
  for i in range(0,len(text)):
      if i+left > len(text)-1 or -i-1-right < -len(text):
          break
      while not text[i+left].isalpha():
          left += 1
      while not text[-i-1-right].isalpha():
          right += 1
      if text[i+left] != text[-i-1-right]:
          return False
  return True


