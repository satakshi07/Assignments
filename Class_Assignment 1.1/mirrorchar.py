# 68. Python Dictionary to find mirror characters in a string Counting the frequencies in a list using
# dictionary in Python

def mirrorChars(string,k):
    
    original="abcdefghijklmnopqrstuvwxyz"
    reverse="zyxwvutsrqponmlkjihgfedcba"
    mirrordict=dict(zip(original,reverse))
    
    prefix=string[:k-1]
    suffix=string[k-1:]
    mirror=""
    for i in range(len(suffix)):
        mirror=mirror+mirrordict[suffix[i]]
    return prefix+mirror

input = 'paradox'
k = 3
print(mirrorChars(input,k))