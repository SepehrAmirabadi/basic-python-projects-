# Sepehr E. Amirabadi
#Comp 1405 B
#assignment 3
#problem 2
#10/30/18

# checks if b is a multiple of a
def ismultiple (a,b):
    if (b%a == 0 ):
        return True;
    else:
        return False; 

#checks if c is a multiple of both a and b
def commonmultiple (a,b,c):
    if (ismultiple(a,c) == True and ismultiple(b,c) == True):
        return True ;
    else:
        return False ;

# prints out multiples of a and b using common multiple 
def test (a,b):
    for x in range (1,101):
        if (commonmultiple (a,b,x) == True):
            print (x)
    return ; 

#user input
a = int (input("enter a number"))
b = int (input("enter a number"))
#function initialization
test(a,b)

        
    



