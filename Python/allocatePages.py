def findPages(arr: [int], n: int, m: int) -> int:
    if len(arr) < m:
        return -1

    low = max(arr)
    high = sum(arr)
    result = -1

    def canDistribute(maxPages):
        students = 1
        curPages = 0
        for pages in arr:
            if curPages + pages <= maxPages:
                curPages += pages
            else:
                students += 1
                curPages = pages
        
        return students <= m

    while low <= high:
        mid = low + ((high-low)//2)
        if canDistribute(mid):
            result = mid
            high = mid-1
        
        else:
            low = mid+1

    return result

