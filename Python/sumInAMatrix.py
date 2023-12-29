class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        n,m = len(nums), len(nums[0])
        for i in range(n):
            nums[i].sort()

        score = 0
        
        for j in range(m):
            maxNum = -math.inf
            for i in range(n):
                maxNum = max(maxNum, nums[i][j])
            score += maxNum
        
        return score