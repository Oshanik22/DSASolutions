from typing import List

def findMaxFruits(arr: List[int], n: int) -> int:
    count = {}
    maxFruits = 0
    left = 0

    for right in range(len(arr)):
        count[arr[right]] = count[arr[right]] + 1 if arr[right] in count else 1

        while len(count) > 2:
            count[arr[left]] -= 1
            if count[arr[left]] <= 0:
                del count[arr[left]]
            left += 1
        
        maxFruits  = max(maxFruits, right-left+1)

    return maxFruits
