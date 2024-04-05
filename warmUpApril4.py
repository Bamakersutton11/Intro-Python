"1) A python while loop is a section of code that runs repeatedly as long as the statement is true."
"2) An iterator works as a starter point for loop codes."
"3) I would fix the "

msg = 1

while msg == 1:
    print(msg)
    msg = input('Enter message: ')
    if msg == 'Stop':
        print("The loop has stopped")



def uberEatsorder():
    orderCart = input("Hello, what would you like to order?: ")
    orderComplete = False
    while orderComplete == False:
        customer_order = input('Would you like to add something?: ')
        if customer_order == 'Y':
            newOrder = input('What would you like to add?: ')
            orderCart += newOrder
        elif customer_order == 'N':
           print(f"Thank you, here is your total: {orderCart}")
        break

i = 0

while i < 4:
    print("April 4")
    i += 1
    print(i)
if i == 10:
    print("Loop stopped.")


def isShmarried():
    womanLastname = 'Smith'
    manLastname = 'Jackson'
    while womanLastname == 'Smith':
        print("This woman is not married ")



