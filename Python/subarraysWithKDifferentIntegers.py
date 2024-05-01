class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(x):
            count = {}
            res = 0
            left = 0

            if x<0: return 0

            for right in range(len(nums)):
                count[nums[right]] = count.get(nums[right], 0) + 1

                while len(count) > x:
                    count[nums[left]] -= 1
                    if count[nums[left]] <= 0:
                        del count[nums[left]]
                    left += 1
                
                res += right-left+1
            
            return res
        
        return helper(k) - helper(k-1)