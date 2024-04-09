# Async Activity April 8th, 2024

# 1. In your own words, describe what a while loop is?

"A while loop is a loop that repeats itself for as long as a condition is met."

#2. Create a function that uses a while loop to determine if a user has typed in 
# the the correct word guess. If the user types in the wrong word, your program 
# should inform them that their guess was inccorect and to try again, but if the
# user guesses the word correctly, your program shoul tell the user they have 
# guessed correctly and have won the game, stopping the loop.

def wordCheck():
    wordEntered = input('Enter word: ')
    correctWord = 'Bright'
    while wordEntered != correctWord:
        wordEntered = input('Please try again: ')
    if wordEntered == correctWord:
        print('This word is correct. Congratulations.')

wordCheck()

