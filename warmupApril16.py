# Warm up Tuesday April 16th, 2024.

import random

# 1. In your own words, explain the difference between an Python For Loop and a
# Python While Loop.

"The difference between a For loop and a while loop is "

# 2. Create a loop that will iterate over a list of numbers. For evey number in your loop,
# it should multiply that number by 3. 
def mulitplyNumb():
    numbers = [1,2,3,4,5,6,7]
    for digit in numbers:
            print(digit*3)

#mulitplyNumb()

# 3. Use the following code snippet below to create a guessing game function. 
# The code below will generate a random number for you. You must write a loop that will
# ask the user to input their guess, if they guess incorrectly, the program will repeat 
# itself and ask the user to guess again. The program should continue to ask them to
# guess until they've gotten it correctly. Once they guess the correct number the program
# will congratulate them and the loop will stop. 

#keywords
    # program will repeat itself(while loop)
    # input
        # input = str(), so add int() before input()
    


# generates a random number between 1 and 10

def numberGuess():
    randomNumber = random.randint(1, 10)
    print(f'Random number value is: {randomNumber}')

    i = int(input("Enter your guess number: "))

    while i != randomNumber:
        int(input("Please try again: "))
    if i == randomNumber:
        print("You have the correct number.")
numberGuess()