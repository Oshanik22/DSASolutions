class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums) 

        def canSplit(largestSum):
            count = 1
            currSum = 0

            for num in nums:
                if currSum + num <= largestSum:
                    currSum += num
                else:
                    count += 1
                    currSum = num
            
            return count <= k

        while low <= high:
            mid = low + (high-low)//2

            if canSplit(mid):
                high = mid-1
            
            else:
                low = mid + 1
            
        return low