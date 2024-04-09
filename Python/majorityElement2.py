class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        countMap = defaultdict(int)

        for num in nums:
            countMap[num] += 1

            if len(countMap) <= 2:
                continue
            
            newDict = defaultdict(int)
            for key, value in countMap.items():
                if countMap[key] > 1:
                    newDict[key] = countMap[key] - 1

            countMap = newDict


        result = []
        for element in countMap:
            if nums.count(element) > len(nums)//3:
                result.append(element)

        return result