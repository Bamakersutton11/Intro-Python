import random

# Async work Monday March 18th, 2024.

#1. Create a function that will count the number of characters in a string
# that is passed in by a user. The string value can be passed in either as 
# a paramter or by using the input function.
 
def characterCount():
    characterNumb = input("Enter characters: ")
    strCount = len(characterNumb)
    print(strCount)

characterCount()
# You must be write down and explain how your program 
# works in complete sentences in order to get full credit. 

"My program takes in the characters and then uses the len() function to count the number of letters of the words that I input."

# 2. Use your notes, W3schools, and what we have learned in class to develop
# a simple rock, paper, scissors game. Your game should allow the user to enter a letter
# that will represent the values rock, paper, and scissors (ex. r = rock, p = paper, s= scissors).

#keywords:
# value
# variables
# enter == input()

def rock_paper_scissors():
    RPS = input()
    if RPS == "r":
        print("Rock")

random.randrange()

# EXTREMELY IMPORTANT NOTE
# at the top of you page write import random
# use the random.randrange(1,3) function to develop your random value logic 
# for your rock, paper, scissor game. 

# Please describe the steps you took, or if you weren't able to complete this activity,
# the steps you would've taken to solve this problem in complete sentences. 
# This must be completed in order to get full credit.  