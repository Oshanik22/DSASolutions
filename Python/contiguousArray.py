class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sums = {0:-1}
        maxLen = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1

        prefixSum = 0

        for i in range(n):
            prefixSum += nums[i]
            if prefixSum in sums:
                #If at some past point, the sum was also the same, that means that the sum of all the elements from that point to this point is 0, which means that it has equal number of 0s and 1s since its a binary array
                startIdx = sums[prefixSum]
                maxLen = max(maxLen, (i-startIdx))
            else:
                sums[prefixSum] = i

        return maxLen
