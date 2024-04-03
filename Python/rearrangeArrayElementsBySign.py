class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0 for _ in range(len(nums))]

        posIdx = 0
        negIdx = 1

        for num in nums:
            if num < 0:
                result[negIdx] = num
                negIdx += 2
            else:
                result[posIdx] = num
                posIdx += 2

        return result