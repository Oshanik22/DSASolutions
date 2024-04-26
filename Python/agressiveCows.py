def aggressiveCows(stalls, k):
    stalls.sort()
    low = 1
    high = 1000000000

    def canPlace(dist):
        cows = 1
        prevCow = stalls[0]

        for i in range(1, len(stalls)):
            if stalls[i]-prevCow >= dist:
                cows += 1
                prevCow = stalls[i]
            
            if cows == k:
                return True
        
        return False

    while low <= high:
        mid = low + (high-low)//2
        if canPlace(mid):
            low = mid+1
        else:
            high = mid-1
    
    return high