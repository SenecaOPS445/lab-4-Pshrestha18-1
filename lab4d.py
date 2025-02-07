#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

def first_five(s):
    return s[:5]

def last_seven(s):
    return s[-7:]

def middle_number(n):
    return str(n)[1:3]

def first_three_last_three(s1, s2):
    return s1[:3] + s2[-3:]

if __name__ == '__main__':
    print(first_five(str1))  # Output: Hello
    print(first_five(str2))  # Output: Senec
    print(last_seven(str1))  # Output: World!!
    print(last_seven(str2))  # Output: College
    print(middle_number(1500))  # Output: 50
    print(middle_number(1.50))  # Output: .5
    print(first_three_last_three(str1, str2))  # Output: Helege
    print(first_three_last_three(str2, str1))  # Output: Send!!
