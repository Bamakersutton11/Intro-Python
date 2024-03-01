def gradeBook(grades):
    if grades >= 60 and grades <= 69:
        print('D')
    elif grades >= 80 and grades <= 89:
        print('B')
    elif grades >= 70 and grades <= 79:
        print('C')
    elif grades >= 90 and grades <= 100:
        print('A')
    elif grades > 100:
        print('Error: No grades above 100')
    else: 
        print('F')

gradeBook(101)

membership_level = ['bronze'+ 'silver' + 'gold' + 'platinum']
bronzeBenefits = []