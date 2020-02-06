import mystack
def isvalid(string):
    list1 = []
    for letter in string:
        if len(list1) == 0 and (letter == ')' or letter == ']' or letter == '}'):
            return False;
            break
        if letter == '(' or letter == '[' or letter == '{':
            list1.append(letter)
        elif letter == ')' or letter == ']' or letter == '}':
            if list1[len(list1)-1] == '(' and letter == ')' or list1[len(list1)-1] == '[' and letter == ']' or list1[len(list1)-1] == '{' and letter == '}':
                list1.pop(len(list1)-1)
    return len(list1)==0
