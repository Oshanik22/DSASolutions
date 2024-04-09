class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        currMin, currMax = 1,1

        for num in nums:
            temp = currMax*num
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(temp, currMin*num, num)
            result = max(currMax, result)

        return result