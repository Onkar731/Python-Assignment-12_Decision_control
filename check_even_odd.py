"""
Write a python script to check whether a given number is even or odd
"""

# taking input from the user
num = int(input("Enter a number : "))

# evaluating whether a given number is even or odd
if num%2 == 0 :
    print(num, "is EVEN")
else :
    print(num, "is ODD")