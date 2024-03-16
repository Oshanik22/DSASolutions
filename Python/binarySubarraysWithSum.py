class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSumSet = {0:1}
        count = 0
        prefixSum = 0

        for num in nums:
            prefixSum += num
            req = prefixSum - goal
            if req in prefixSumSet:
                count += prefixSumSet[req]
            prefixSumSet[prefixSum] = 1 if prefixSum not in prefixSumSet else prefixSumSet[prefixSum] + 1
        
        return count