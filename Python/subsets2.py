class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.findSubset(0, [], result, nums)

        return result

    def findSubset(self, idx, path, result, nums):
        result.append(path)

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.findSubset(i+1, path + [nums[i]], result, nums)

    