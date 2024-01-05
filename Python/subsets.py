class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.findSuperset(0, [], result, nums)
        return result

    def findSuperset(self, idx, path, result, nums):
        result.append(path)
        for i in range(idx, len(nums)):
            self.findSuperset(i+1, path + [nums[i]], result, nums)