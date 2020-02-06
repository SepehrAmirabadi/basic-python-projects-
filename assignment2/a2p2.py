#assignment 2 - problem 2
# 01/10/18
#Sepehr Amirabadi

#variable decleration (arrays used to lower number of if statements)
name = input ("welcome to Dino's International Doughnut Shoppe!!\nPlease enter your name to begin: ")
orderfinished = 0
total = 0
Orderdetails = []
price = [3.50, 2.25,4.05,1.99]
doughnuts = ["Chocolate-dipped Maple Puff's","Strawberry Twizzler's","Vanilla Chai Strudel's","Honey-drizzled Lemon Dutchie's"]

#asks customer for order until order is compleate
while (orderfinished == 0):
    choice  = int(input ("Please select a doughnut from the following menu:\n1. Chocolate-dipped Maple Puff ($3.50 each)\n2. Strawberry Twizzler ($2.25 each)\n3. Vanilla Chai Strudel ($4.05 each)\n4. Honey-drizzled Lemon Dutchie ($1.99)\n5. No more doughnuts\n"))
    if (choice >0 and choice <5):
        quantity = int(input ("how many " + doughnuts[choice-1] + " would you like to purchase: "))
        total += quantity*price[choice-1]
        Orderdetails.append (("Items puchased: " + str(quantity) + " " + doughnuts[choice-1]))
    elif (choice ==5):
        orderfinished = 1
    else:
        print ("Sorry that is not a valid order number")
        
#output reciept
print (name + " , here is your recipt")
print ("------------------------------------")
print ("          Order Details             ")
print ("------------------------------------")
for a in range (0,len(Orderdetails)):
    print (Orderdetails[a])
print ("Total: " + str(total)+ "$")
