def giftCard_add5_toBalance(user_Giftcard):
    newBalance = user_Giftcard + .50
    print(f'You now have {newBalance} dollars on your gift card.')

giftCard_add5_toBalance(17)

# Argument = facts = data 

import datetime

x = datetime.datetime.now()

print(f"You made your transaction on " + x)