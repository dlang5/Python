from service_fees import FastOrderDeliverySystem # import classes
from service_fees import Users
import tkinter as tk # import GUI

root = tk.Tk()
logo = tk.PhotoImage(file="bell.gif")

w1 = tk.Label(root, image=logo).pack(side='right')

explanation = "Welcome to Live Mas"

w2 = tk.Label(root, text=explanation).pack()

button = tk.Button(
    text="Ok!",
    bg="white",
    fg="black",
    command = root.destroy
)
button.pack()
root.mainloop()


# dictionary of menu
inventory = {1:('Chalupa', 2.99), 2:('MexiMelt', 3.99),
             3:('Crunch Wrap', 2.99), 4:('Gordita', 2.99),
             5:('Power Bowl', 5.99), 6:('Regular Taco', .99),
             7:('Doritos Locos Taco', 1.99), 8:('Quesadilla', 1.99)}

print("Welcome to the Taco Bell Delivery app.\nWhat would you like to order?")

# print menu
for k,v in inventory.items():
   # print('%-20s{}) {}: $ {}'.format(k, v[0], v[1]))
    print("%d: %-20s $%d.99" % (k, v[0], v[1]))

# initialize values of each item in cart
cart = [0,0,0,0,0,0,0,0]

#choose multiple items
keep_choosing = 'Y'
while keep_choosing == 'Y':
    choice = int(input('\nWhat is your choice: '))

    # determine number of each item, change appropriate value in cart list
    if choice in inventory.keys():
        number = int(input(str(inventory[choice][0]) + " @ $" +
                           str(inventory[choice][1]) + "\nHow many? "))
        cart[choice-1] += number
    else:
        print("Invalid choice")

    # updated cart
    keep_choosing = input("Still choosing? (y/n): ").upper()
    
# order time
time = FastOrderDeliverySystem.schedule()

# create object
TacoBell = FastOrderDeliverySystem(cart, inventory, time)

# call total function from module
TacoBell.total(cart, inventory, time)


u1 = Users.getData()




