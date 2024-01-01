class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x

        while low <= high:
            mid = low + (high - low)//2
            sq = mid**2
            if sq == x:
                return mid
            if sq > x:
                high = mid - 1
            else:
                low = mid + 1
        return high