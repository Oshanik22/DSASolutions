class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high  = 0, len(nums)-1
        result = nums[0]
        while low <= high:
            mid = (low + high) // 2
            if nums[low] < nums[high]:
                result = min(result, nums[low])
                break
            result = min(result, nums[mid])
            if nums[low] <= nums[mid]:
                low = mid+1
            else:
                high = mid-1

        return result