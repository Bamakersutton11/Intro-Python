# For Loops --> A for loop is a type of loop that will 

birdGame = ['duck', 'duck', 'goose', 'duck', 'duck']

for x in birdGame:
    if x == 'goose':
        print(f"found the goose at index {birdGame.index('goose')}")
        continue
    print(x)

Spades = ['1','2','3','4','SJ','SQ','SK','S']


def customerReturn():
    # when a receipt number is entered,
    # remove the items from customers credit card.
    userReturn = input("What would you like to learn? ")

    receipt = ['TV', 'Game', 'Controller', 'Movie']

    for item in receipt: 
        if item == userReturn:
            
