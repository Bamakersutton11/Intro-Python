# 1) One issue is that the function definition has no colon after
# the parentheses to make the function start. It also doesn't have a
# recognized parameter. The function does not require nor recognize using the
# print() for function calls.

# def goodMorning()
# print('Good morning, stranger')

#print goodMorning(name)

# Better example below:

def goodMorning(name):
    print(f"Good Morning, {name}")

goodMorning('Braheem')

# 2) The difference between a parameter and an argument is that
# the argument is the actual data, while the parameter is the container
# for that data. 


time = float(input('What time is it?'))

if time < 10.00:
    print('Welcome to class.')
else: 
    print('Class is over')

menu = ['Cheesesteak', 'Cheese fries', 'Cheeseburger']

userChoice = input()