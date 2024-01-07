from collections import *
def search(pat, txt):
    chars = {}
    txtChars = Counter(txt)
    count = 0
    i,j = 0, 0
    
    while j<len(pat):
        if pat[j] not in chars:
            chars[pat[j]] = 0
        
        chars[pat[j]] += 1

        if j-i+1 < len(txt):
            j += 1
            continue
        
        if j-i+1 == len(txt):
            if chars == txtChars:
                count += 1
            chars[pat[i]] -= 1
            i += 1
            j += 1
    return count

print(search("aabaabaa", "aaba"))