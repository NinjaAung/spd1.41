'''
Given a number n, determine what the nth prime is.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

If your language provides methods in the standard library to deal with prime
numbers, pretend they don't exist and implement them yourself
'''

'''
variable : value

prime_beg : list, first three prime nums
number : int, how many numbers till the last prime
current_num : int, what number could be the prime
prime_num : int, the most recent prime of the while loop

assumptions: if no prime is found return otherwise return the last index
'''
def is_prime(n) :
    if n % 2 == 0 or n % 3 == 0 : 
        return False
    i = 5
    while i**2 <= n : 
        if n % i == 0 or n % (i + 2) == 0 : 
            return False
        i += 6
    return True
  
def prime(number):
    if number <= 0:
        raise ValueError("No Zeroth Prime")

    prime_beg =[2,3,5]
    if number <= 3:
        return prime_beg[number-1]

    number -= 3
    current_num = prime_beg[len(prime_beg)-1]
    prime_num = None

    while number > 0:
        current_num += 1
        if is_prime(current_num):
            prime_num = current_num
            number -= 1

    return prime_num