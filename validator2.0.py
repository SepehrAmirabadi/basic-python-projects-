import mystack
def isvalid(string):
    validbrackets = {'(':')','[':']','{':'}'}
    list1 =[]
    for letter in string:
        try:
            closing = validbrackets[list1.pop()]
        except:
            return False;
        if letter in validbrackets:
            mystack.push (list1,letter)
        elif (closing != letter):
            return False
    if(len(list1)==0):
        return True;








































#old logic
##    list1 =[]
##    for letter in string:
##        if letter == '(' or letter == '[' or letter == '{'or letter == '}' or letter == ']' or letter ==')' :
##            list1.append (letter)
##    if (len(list1) == 0):
##        return True;
##    if (len(list1) % 2 == 0):
##        while (len(list1) > 0):
##            for value in array-1:
##                if (list1 [x] == '(' and list1 [x+1] ==')') or (list1 [x] == '{' and list1 [x+1] =='}') or (list1 [x] == '[' and list1 [x+1] ==']') :
##                    list1.pop(x)
##                    list1.pop(x+1)
##            if y==0 and x == len(list1)-2:
##                return False;
##                break
##    else:
##        return False;
##    if (len(list1)==0):
##        return True;
##    print(list1)

##
##closingbracket = mystack.pop(list1)
##            openingbracket = myqueue.dequeue(list1)
##            if (closingbracket == ')'and openingbracket != '(') or (closingbracket == ']'and openingbracket != '[') or (closingbracket == '}'and openingbracket != '{'):
##                return False;
##                break
##            elif((closingbracket == ')'and openingbracket == '(') or (closingbracket == ']'and openingbracket == '[') or (closingbracket == '}'and openingbracket == '{') and len (list1)== 0):
##                return True;
##                break
