def startwords(string):
    sentences = []
    startingword = []
    sentences = (string.split(". "))
    for line in sentences:
        words = line.split(" ")
        words.pop()
        if words[0] not in startingword:
            startingword.append(words[0])            
    return startingword;

def endwords(string):
    sentences = []
    endingword = []
    sentences = (string.split("."))
    sentences.pop(len(sentences)-1)
    for line in sentences:
        words = line.split(" ")
        words.pop(0)
        if words[len(words)-1] not in endingword:
            endingword.append(words[len(words)-1])
    return endingword;


            
