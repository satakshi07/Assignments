# 67. Python | Remove all duplicates words from a given sentence

def dup_word(string):
    slist=string.split()
    uword=""
    for w in slist:
        if w not in uword:
            uword=uword+" "+w
    return uword
s="Swapnil Sapna Swapnil Smita Godavari Bhagwan"
print(dup_word(s))