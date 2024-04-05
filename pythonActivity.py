def enterPasscode():
    Passcode = int(input())    
    correctCode = 112106 
    while Passcode != correctCode:
        Passcode = int(input("Please try again. "))
    if Passcode == correctCode:
        print("You may now visit the website.")
    
enterPasscode()