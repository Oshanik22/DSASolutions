class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start = nums[0]
        result = []

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    result.append(str(start))

                else:
                    result.append(str(start) + "->" + str(nums[i-1]))

                start = nums[i]

        if start == nums[-1]:
            result.append(str(start))

        else:
            result.append(str(start) + "->" + str(nums[-1]))

        return result