def combsort(list):
    gap = len(list)
    shrink = 1.3
    Sorted = False
    while Sorted == False:
        gap = int(gap/shrink)
        if gap >1:
            Sorted=False
        else:
            gap = 1
            Sorted = True
            
        i = 0
        while i + gap <len(list):
            dist1 = ((list[i][0]**2)+(list[i][1]**2))**(1/2)
            dist2 = ((list[i+gap][0]**2)+(list[i+gap][1]**2))**(1/2)
            if dist1 > dist2:
                temp = list[i]
                list [i] = list[i+gap]
                list [i+gap] = temp
                Sorted = False
            i +=1

                
            
    
