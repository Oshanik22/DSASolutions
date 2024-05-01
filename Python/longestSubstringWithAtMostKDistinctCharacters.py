def kDistinctChars(k, str):
    count = {}
    maxLen = 0
    left = 0
    
    for right in range(len(str)):
        count[str[right]] = count.get(str[right],0)+1

        while len(count) > k:
            count[str[left]] -= 1
            if count[str[left]] <= 0:
                del count[str[left]]
            left += 1

        maxLen = max(maxLen, right-left+1)

    return maxLen


