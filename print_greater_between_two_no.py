"""
Write a python script to print greater between two numbers.
Print number only once even if the numbers are the same.
"""

# taking two numbers from the user
num1, num2 = int(input("Enter two numbers : ")), int(input())

# evaluating a greater number between two numbers
if num1 > num2 :
    print(num1, "is GREATER")
elif num2 > num1 :
    print(num2, "is GREATER")
else :
    print("Both are the same : ", num1)