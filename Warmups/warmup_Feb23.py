# 1) The two parts needed to create a function are a definition and a function call.
# A function defintion contains all of the steps that are needed for the function to work
# and a function call executes the all steps.

def signUp():
    userName = input('Email or Usename: ')
    userPassword = input('Password: ')

# signUp()

def doMath(number):
    result = 10 + number
    print(result)

# doMath(133)
# 2) The difference between a function parameter and a function argument are that
# the arguments themselves are the actual data that we can add and , while the parameters are the 
# 3)

def futureMsg(name, age):
    futureAge = age + 10
    print(f'Good morning {name}, you will be {age} years old in 10 years')

futureMsg('Braheem', 17)

def passCheck(userPIN, userName):
    PIN = 112106
    Name = "Heemy"
    if userPIN == PIN and userName == Name:
        print("Login Successful")
    elif userName == Name and userPIN != PIN:
        print("PIN is incorrect")
    elif userPIN == PIN and userName != Name:
        print("Name is incorrect")
    else:
        print("Incorrect.")
        
passCheck(1212, "Hem")