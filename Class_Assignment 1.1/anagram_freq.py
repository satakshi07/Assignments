# 66. Python Counter to find the size of largest subset of anagram words

from collections import Counter

def anagramFreq(string):
    slist=string.split()
    
    for i in range(len(slist)):
        slist[i]="".join(sorted(slist[i]))

    freqDict=Counter(slist)
    
    maxfreq=max(freqDict.values())
    
    return maxfreq

# Driver program
if __name__ == "__main__":
    input = 'ant magenta magnate tan gnamate'
    print(anagramFreq(input))