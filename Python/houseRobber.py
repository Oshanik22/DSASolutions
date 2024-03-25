class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.maxMoney(nums, 0, {})
    def maxMoney(self, nums, idx, memoise):
        if idx >= len(nums):
            return 0
        
        if idx == len(nums)-1:
            return nums[idx]

        if idx in memoise:
            return memoise[idx]

        # option 1, we rob the house
        robYes = nums[idx] + self.maxMoney(nums, idx+2, memoise)

        # option 2, we dont rob the house
        robNo = self.maxMoney(nums, idx+1, memoise)

        profit = max(robYes, robNo)

        memoise[idx] = profit
        return profit