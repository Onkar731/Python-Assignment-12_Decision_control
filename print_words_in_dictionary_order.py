"""
Write a python script to print two given words in dictionary order
"""

# taking two words from the user
word1, word2 = input("Enter First Word : "), input("Enter Second Word : ")

# printing words in dictionary order
if word1 < word2 :
    print(word1, word2, sep='\n')
else :
    print(word2, word1, sep='\n')