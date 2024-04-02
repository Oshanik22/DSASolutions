class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        if not nums:
            return 0
        maxLength = 1

        for i in range(len(nums)):
            num = nums[i]
            for j in range(i):
                if nums[j]<num:
                    currLength = dp[j]+1
                    if currLength > dp[i]:
                        dp[i] = currLength
                        maxLength = max(dp[i], maxLength)

        return maxLength
            

