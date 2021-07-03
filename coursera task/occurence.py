
# to find a more than two Occurrence then returns true otherwise false
def occurence(word, sentenance):
    if(sentenance.find(word) != -1):
        firstOccur = sentenance.find(word)+len(word)
        print(firstOccur)
        secondOccur = sentenance[firstOccur:len(sentenance)]
        print(secondOccur)
        if(secondOccur.find(word) != -1):
            #print("more thn two occurence found")
            return True
        else:
            #print("No more than two occurence found")
            return False
    else:
        #print("No more than two occurence found")
        return False


print(occurence("by", "bybybyby"))
