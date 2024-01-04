class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                return True
            
            if nums[mid] == nums[right]:
                right -=1

            # check if we are in the left sorted array
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            # if not in left sorted array, that means we are in right sorted array
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        
        return False