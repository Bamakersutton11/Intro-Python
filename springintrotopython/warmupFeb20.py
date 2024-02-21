laundryList = ['towel', 'rag', 'clothes', 'laundry basket', 'detergent']

print(laundryList[3])

# Notes 
# 1. Take in user name --> input()
# 2. Reverse and print the user name --> 

def reverseName():
    name =  input('What is your name: ')[::-1]
    print(name)

reverseName()

def cheeseCake():
    print("Here's how to make a cheesecake...")

def securityLogin():
    Pin = input('Please enter your pin: ')
    return Pin
securityLogin()

def companyLogin(name):
    print(f'hello {name}')

companyLogin('Braheem')

def math(number):
    result = number + 10
    print(result)

math(11)

debit = 10000
money = int(input())
print(debit - money)
