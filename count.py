def countsort(list):
    dict1 ={}
    templist =[]
    newlist=[]
    for value in list:
        if value in dict1.keys():
            dict1[value]+=1
        else:
             dict1[value]=1
             templist.append (value)

    while len(templist)>0:
        lowestvalue = templist[0]
        for value in templist:
            if value< lowestvalue:
                lowestvalue = value
        for x in range (0,dict1[lowestvalue]):
            newlist.append(lowestvalue)
        templist.remove(lowestvalue)
    return newlist



    
