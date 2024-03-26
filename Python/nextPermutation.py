class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bPoint,n = -1, len(nums)

        for i in range(n-2, -1, -1):
            if nums[i] >= nums[i+1]: continue
            bPoint = i

            for j in range(n-1, i, -1):
                if nums[j] > nums[bPoint]:
                    nums[j], nums[bPoint] = nums[bPoint], nums[j]
                    break
            break
        nums[bPoint+1:] = reversed(nums[bPoint+1:])
