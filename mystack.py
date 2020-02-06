def push (stack,value):
    stack.append(value)
def pop (stack):
    if len(stack)>0:
        return stack.pop(len(stack)-1);
    else:
        return None;
def isempty(stack):
    if len(stack)>0:
        return False;
    else:
        return True;
def peak(stack):
    if len(stack)>0:
        return stack[len(stack)-1];
    else:
        return None
    
    
