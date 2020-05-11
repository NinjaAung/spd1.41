'''
A Pythagorean triplet is a set of three natural numbers, {a, b, c}, for which,

a**2 + b**2 = c**2

and such that,

a < b < c


Given an input integer N, find all Pythagorean triplets for which a + b + c = N.
s
For example, with N = 1000, there is exactly one Pythagorean triplet for which a + b + c = 1000: {200, 375, 425}.


variable : value
a : int, base, a + b  =  c
b : int, side,a + b  =  c
c : int, hypotneusea + b  =  c
number : int, sum of all parts of the triangle
triplets : list, items consist of all list

'''
import math

def triplets_with_sum(number):
    triplets = []
    for b in range(number):
        for a in range(1, b):
            if a + b > number:
                if a > number:
                    break
                continue
            c = math.sqrt( a * a + b * b)
            if c % 1 == 0:
                if  a + b + int(c) == number:
                    triplets += [[a, b, int(c)]]
                    print(triplets)
    return triplets
