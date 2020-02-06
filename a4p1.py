queuemax= 10
def enqueue(queue,value):
    if len (queue)<queuemax:
        queue.append(value)
        return True;
    else:
        return False;
def dequeue (queue):
    if len (queue)>0:
        first  = queue.pop(0)
        return first;
    else:
        return None;
def peek(queue):
    if len (queue)>0:
        first  = queue[0]
        return first;
    else:
        return None;
def isempty(queue):
    if len (queue)>0: 
        return False;
    else:
        return True;

def multienqueue(queue,items):
    i = 0
    for value in items:
        if queuemax> len (queue):
            queue.append(value)
            i+=1
    return i;
def multidequeue (queue,number):
    list = []
    for x in range (0,number-1):
        list.append(queue.pop(x))
    return list;
        
        
        
