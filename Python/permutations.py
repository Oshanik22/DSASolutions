class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        picked = set()
        curr_length = 0
        curr_perm = []
        result = []

        self.findPerm(curr_length, curr_perm, picked, result, nums)

        return result

    def findPerm(self, curr_length, curr_perm, picked, result, nums):
        if curr_length == len(nums):
            result.append(curr_perm)
        
        for i in range(len(nums)):
            if i not in picked:
                picked.add(i)
                self.findPerm(curr_length+1, curr_perm + [nums[i]], picked, result, nums)
                picked.remove(i)
            
