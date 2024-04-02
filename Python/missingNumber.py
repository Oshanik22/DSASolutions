class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = (n * (n+1))//2
        sumOfNums = sum(nums)

        return totalSum - sumOfNums


'''
     .
[3,0,1]
 0 1 2

'''