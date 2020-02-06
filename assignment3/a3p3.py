# Sepehr E. Amirabadi
#Comp 1405 B
#assignment 3
# Problem 3
#10/30/18


list = ["A","B", "C", "D", "E", "F","G","H","I","J"]
def slice (list,b,c):
    slicedlist = [] #declare new list
    if (b>=0 and b<=len(list)-1) and (c>=b and c<len(list)-1):
        for x in range (b,(c+1)):
            slicedlist.append(list[x]) # adding values from previous array that are within range
    return slicedlist; # return new list


#test case
print ("example slicing")
print (slice(list,0,9))
print (slice(list,3,4))
print (slice(list,4,3))
print (slice(list,3,8))
print (slice(list,4,4))
            


