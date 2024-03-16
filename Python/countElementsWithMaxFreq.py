class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxFreq = -math.inf
        freqMap = Counter(nums)
        count = 0
        for key in freqMap:
            if freqMap[key] > maxFreq:
                maxFreq = freqMap[key]

        for key in freqMap:
            if freqMap[key] == maxFreq:
                count += freqMap[key]
        
        return count