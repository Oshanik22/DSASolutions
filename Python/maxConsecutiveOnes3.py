class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        nums = [1,1,1,0,0,0,1,1,1,1,0]
        '''

        maxLength = 0
        left = 0
        zero = 0

        for right in range(len(nums)):
            if nums[right]==0:
                zero += 1

            while zero > k:
                if nums[left] == 0:
                    zero -= 1
                
                left += 1

            maxLength = max(maxLength, right-left+1)
        
        return maxLength
