class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if not nums:
            return None
        if n == 1:
            return nums

        result = [1 for _ in range(n)]

        leftProduct = nums[0]
        rightProduct = nums[n-1]

        for i in range(1, n):
            result[i] *= leftProduct
            leftProduct *= nums[i]
        
        for j in range(n-2, -1, -1):
            result[j] *= rightProduct
            rightProduct *= nums[j]

        return result