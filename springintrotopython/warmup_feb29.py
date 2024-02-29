# 1) The if statement in python is "IF" something meets a
# certain criteria, it will executes these certain instructions.
# While else is just if something doesn't meet the criteria of the if statement
# it will do what the else says instead.

def highScore():
    high_score = 3000
    userScore = int(input('What is your score? '))
    if userScore == high_score: 
        print("You have reached the high score!")
    elif userScore >= high_score:
        print("You have achieved a new high score!")
    else:
        print("You have not reached the high score.")

highScore()