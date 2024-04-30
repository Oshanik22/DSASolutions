class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(x):
            if x<0: return 0
            left=0
            count = 0
            curCount = 0

            for right in range(len(nums)):
                curCount += (nums[right]%2)

                while curCount > x:
                    curCount -= (nums[left]%2)
                    left += 1

                count += (right-left+1)
            
            return count
        
        return helper(k) - helper(k-1)