class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        lower, upper = -1,-1
        
        # find lower bound
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                lower = mid
                high = mid-1

            elif nums[mid] > target:
                high = mid-1

            else:
                low = mid+1

        #find upper bound
        low,high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) //2
            if nums[mid] == target:
                upper = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid-1

        return [lower, upper]
