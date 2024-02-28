def passWord():
    passCode = 'get_this_money'
    Correctpasscode = input('Enter your password: ')
    if Correctpasscode == passCode:
        print("Access Granted")
    else:
        print("Access Denied")

passWord()