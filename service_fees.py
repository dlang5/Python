import datetime # receipt date and time
import random # randint()

#open up capabilities for other types of apps (reservation management)
class RestaurantApps:
    def __init__(self,time,inventory,cart):
        self.time = time
        self.inventory = inventory
        self.cart = cart

#subclass for creating generic apps
class FastOrderDeliverySystem(RestaurantApps):
    # schedule delivery
    def schedule():
        
        month = int(input('\nWhat month will you pick up your order?: '))
        day = int(input('\nWhat day of the month will you pick up your order?: '))
        hour = int(input('\nWhat hour will you pick up your order?: '))
        minutes = int(input('\nWhat number of minutes after the hour will you pick up your order?: '))

        # exception handling
        if month > 12 or month < 1 or day > 31 or day < 1 or hour > 23 or hour < 1 or minutes > 59 or minutes < 0:
            raise Exception("DATE OUT OF SCOPE")

        time = str(str(month) + '/' + str(day) + ' @ ' +
                   str(hour) + ':' + str("{:02d}".format(minutes)))

        return time

    # function to calculate and print receipt info
    def total(self, cart, inventory, time):

        subtotal = 0
        
        # calculate subtotal by multiplying cart and inventory
        for i in cart:
            if i > 0:
                subtotal += cart[i-1] * inventory[i][1]

        print("\nYour Taco Bell Receipt for " + str(datetime.datetime.now().strftime("%Y-%m-%d at %H:%M")))
        print("The order will be delivered on " + time + "\n")

        # print recipt itemized
        for i in cart:
            if i > 0:
                print(str(cart[i-1]) + ' '  + str(inventory[i][0])
                      + ' @ $' + str(inventory[i][1]) + "\n")
                
        print('Subtotal: $ ' + str(round(subtotal,2)))

        tax_amount = .085*subtotal
        print('Tax: $ ' + str(round(tax_amount,2)))

        delivery = 3.99
        print('Delivery Fee: $ ' + str(round(delivery,2)))

        total = subtotal + tax_amount + delivery
        print('Total: $ ' + str(round(total,2)))

        FastOrderDeliverySystem.receipts(cart, subtotal, total, delivery, inventory, time)
        
    # function to write to txt file receipt
    def receipts(cart, subtotal, total, delivery, inventory, time):

        # file open
        f = open(r'receipts.txt', 'w')

        f.write("Your Taco Bell Receipt for " + str(datetime.datetime.now().strftime("%Y-%m-%d at %H:%M")))
        f.write("\nThe order will be delivered on " + time + ".\n\n")
        tax_amount = .085*subtotal

        # write receipt itemized
        for i in cart:
            if i > 0:
                f.write(str(cart[i-1]) + ' '  + str(inventory[i][0]) + ' @ $' + str(inventory[i][1]) + '\n')

        f.write('\nSubtotal: $ ' + str(round(subtotal,2)))

        f.write('\nTax: $ ' + str(round(tax_amount,2)))

        f.write('\nDelivery Fee: $ ' + str(round(delivery,2)))

        f.write('\nTotal: $ ' + str(round(total,2)))
        
        f.close()

# user class for ID system
class Users:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def getData():
        name = input("Enter name to create account: ")
        ID = random.randint(0, 99999999)
        print("Welcome, " + name + str(ID))
      


    
