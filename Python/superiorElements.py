from typing import *
import math

def superiorElements(a : List[int]) -> List[int]:
    rightMax = -math.inf
    result = []

    for i in range(len(a)-1, -1, -1):
        if a[i] > rightMax:
            rightMax = a[i]
            result.append(a[i])

    return result