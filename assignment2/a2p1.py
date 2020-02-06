#assignment 2 - problem 1
# 01/10/18
#Sepehr Amirabadi

#variable decleration (arrays used to lower number of if statements)
name = input ("welcome to Dino's International Doughnut Shoppe!!\nPlease enter your name to begin: ")
orderfinished = 0
price = [3.50, 2.25,4.05,1.99]
doughnuts = ["Chocolate-dipped Maple Puff's","Strawberry Twizzler's","Vanilla Chai Strudel's","Honey-drizzled Lemon Dutchie's"]
# prompts user to pick a variety until a valid descision has been made
while (orderfinished == 0):
    choice  = (input ("Please select a doughnut from the following menu:\n1. Chocolate-dipped Maple Puff ($3.50 each)\n2. Strawberry Twizzler ($2.25 each)\n3. Vanilla Chai Strudel ($4.05 each)\n4. Honey-drizzled Lemon Dutchie ($1.99)\n"))
    if (choice.isdigit() ==True):
        choice = int(choice)
        if (choice >0 and choice <5):
            quantity = int(input ("how many " + doughnuts[choice-1] + " would you like to purchase: "))
            total = quantity*price[choice-1]
            orderfinished = 1
        else:
            print ("Sorry that is not a valid order number")
    else:
        print ("Sorry that is not a valid order number")

#output receipt
print (name + " , here is your recipt")
print ("------------------------------------")
print ("          Order Details             ")
print ("------------------------------------")
print ("Items puchased: " + str(quantity) + " " + doughnuts[choice-1])
print ("Total: " + str(total)+ "$")
