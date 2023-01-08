"""
Write a python script to check whether a given number is divisible by 5 or not
"""

# taking number from the user
num = int(input("Enter a number : "))

# evaluating whether a given number is divisible by 5 or not
if num%5 == 0 :
   print(num, "is divisible by 5")
else :
    print(num, "is not divisible by 5")
