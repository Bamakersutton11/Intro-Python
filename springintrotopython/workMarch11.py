# Intro to Python Async Work
# Monday March 11th, 2024.

# INSTRUCTIONS
# Create a new python file called async_3_11.py
# Answer the following questions. Once you've completed the questions, commit
# and sync your work.
# This activity must be completed by the end of class in order to recieve
# a grade.

# REMEMBER - TAKE YOUR TIME AND DO YOUR BEST! DO NOT GIVE UP! 

# 1. Which Python datacasting function would
# you use if you wanted to convert a string data type
# into an integer data type? Please write your response
# in a complete sentence. 

# You would have to use the int() function that wraps around a string function.

# 2. Create a list called numbCol that contains three (3 ) colors and three (3) numbers.

numnCol = ["red", "blue", "green" , 7, 21, 11]

{} #Curly - These are used for objects
[] #Square - These are used for lists
() #Round - These are used for functions

# 3. You have been hired by a University to create
# a scholarship function. The client would like to provide 
# students a scholarship to their school based on the following
# conditions; 
# - If the user has never gotten a loan before and,
#-  if the user has never been to college before.
# The client would like you to use the logical NOT operator that will
# compare the condtions and return false. If the result is false, the client
# would also like the program to print the message "congrats! you've gotten the scholarship."
# the client has given you the choice on how to enter data for your function.
# you may enter data using input or pass in data into your function as parameters. 

# Compare --> Logical operator - question is asking us to use the NOT operator

# - If the user has never gotten a loan before and,
#-  if the user has never been to college before.

def scholarShip():
    userLoan = bool(input("Have you ever received a loan? True or False: "))
    collegeEnrollment = bool(input("Have you ever been enrolled in college? True or False: "))
    if not (userLoan == True and collegeEnrollment == True):
        print("Congrats! You've gotten a scholarship!")
    elif userLoan == True and collegeEnrollment == False:
        print("We regret to tell you that you do not meet the requirements for a scholarship.")
    elif userLoan == False and collegeEnrollment == True:
        print("We regret to tell you that you do not meet the requirements for a scholarship.")
    else:
        print("We regret to tell you that you do not meet the requirements for a scholarship.")

scholarShip()

