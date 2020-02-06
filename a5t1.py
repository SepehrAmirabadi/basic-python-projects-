def cachedfactorial (num,dict):
    if num ==1 :
        dict [1] = 1
        return 1
    if num in dict.keys():
        return dict [num]
        dict [num] = num*cachedfactorial(num-1,dict)
    else:
        return num*cachedfactorial(num-1,dict)
        dict[num] =num*cachedfactorial(num-1,dict)

dict = {}
print (cachedfactorial(5,dict))
print(cachedfactorial(6,dict))


    
