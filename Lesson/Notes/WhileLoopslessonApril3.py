i = 1 # i is an iterator; or starting point

while i < 17:
    print(i)
    i += 1

inventory_hangers = 2
while inventory_hangers > 0:
    purchase = input("Would you like to purchase a hanger? ")
    if purchase == 'Yes':
        inventory_hangers -= 1
        print(f'Hangers left: {inventory_hangers}')
print("Out of stock")