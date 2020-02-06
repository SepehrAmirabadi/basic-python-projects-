letterfreq = {}
wordfreq = {}
wordlist =[]
def load(str) :
    global letterfreq
    global wordfreq
    global wordlist
    letterfreq = {}
    wordfreq = {}
    wordlist =[]
    word = ""
    file = open(str,"r")
    for line in file :
        word+=line
    letters = word.strip(" ")
    wordlist = word.split(" ")
    for words in wordlist:
        if words in wordfreq:
            wordfreq[words] +=1
        else:
            wordfreq[words] =1

    for letter in letters:
        if letter in letterfreq:
            letterfreq[letter]+=1
        else:
            letterfreq[letter] =  1

def commonword(list):
    cword = list[0]
    if list[0] in wordfreq:
        cfreq = wordfreq[list[0]]
    for word in list:
        if word in wordfreq:
            if wordfreq[word] >= cfreq:
                cfreq = wordfreq[word]
                cword = word
    if cword in wordfreq:
        return cword

def commonpair (string):
    nextwordfreq ={}
    highestfreq = 0
    for x  in range (0, len(wordlist)-1):
        if wordlist[x] == string:
            if wordlist[x+1] in nextwordfreq:
                nextwordfreq[wordlist[x+1]]+=1
            else:
                nextwordfreq[wordlist[x+1]] = 1
    for word in nextwordfreq.keys():
        if nextwordfreq[word] > highestfreq:
            highestfreq = nextwordfreq[word]
            highestword = word
    if highestfreq != 0:
        return highestword
        

def commonletter (list):
    cletter = list[0]
    if list [0] in letterfreq:
        cfreq = letterfreq[list[0]]
    for letter in list:
        if letter in letterfreq:
            if letterfreq[letter] >= cfreq:
                cfreq = letterfreq[letter]
                cletter = letter
    if cletter in letterfreq:
        return cletter

def countall():
    return len(wordlist)
def countunique():
    return len (wordfreq)



    

    
