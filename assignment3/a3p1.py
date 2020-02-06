#Sepehr E. Amirabadi
#Comp 1405 B
#Assignment 3
#problem 1
# 10/30/18

#opening file
text = input ("enter the file name (do not include .txt the program will do that itself)")
sfile = open (text+".txt","r")

#variable decleration
fn = []
ln = []
mg =[]
ag = []
eg = []
highestgrade = 0
higheststudent = 0
lowestgrade = 100
loweststudent =0
passedstudents = 0
finalgrade = []
sum = 0
# collecting and orginizing student names and grades
for num, line in enumerate(sfile) :
    if (num % 6 == 0):
        fn.append(line.strip())
    elif (num % 6 == 1):
        ln.append(line.strip())
    elif (num % 6 == 3):
        mg.append(float(line.strip()))
    elif (num % 6 == 4):
        ag.append(float(line.strip()))
    elif (num % 6 == 5):
        eg.append(float(line.strip()))

for x in range (0,len(mg)):
    #avg calculations
    finalgrade.append((mg[x]*0.25)+(ag[x]*0.25)+(eg[x]*0.5)) #calculating finalgrade of students 
    sum += finalgrade [x]
    #determining higest and lowest students
    if (finalgrade[x]> highestgrade):
        higheststudent =x
        highestgrade = finalgrade[x]
    elif (finalgrade[x]< lowestgrade):
        lowestgrade = finalgrade[x]
        loweststudent = x
    #determining number of passes and fails
    if finalgrade [x] >= 50 and  eg[x]>=50:
        passedstudents += 1
        
#output summary 
print ("NUMBER PASSED: " + str (passedstudents))
print ("NUMBER FAILED: " + str (len (mg) - passedstudents))
print ("AVG FINAL GRADES: " + str (sum/len(mg)))
print ("HIGHEST GRADE: " + fn [higheststudent] + " " + ln [higheststudent] + "-" + str(highestgrade))
print ("LOWEST GRADE: " + fn [loweststudent] + " " + ln [loweststudent] + "-" + str(lowestgrade))




    
        

        
            
    
    
