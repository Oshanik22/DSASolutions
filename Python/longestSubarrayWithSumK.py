from sys import *
from collections import *
from math import *

def getLongestSubarray(nums: [int], k: int) -> int:
    sums = {}
    prefixSum = 0
    maxLength = 0

    for i,num in enumerate(nums):
        prefixSum += num
        if prefixSum == k:
            maxLength = max(maxLength, i+1)

        rem = prefixSum - k

        if rem in sums:
            maxLength = max(maxLength, i-sums[rem])

        if prefixSum not in sums:
            sums[prefixSum] = i

    return maxLength