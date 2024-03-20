class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = Counter(tasks)
        maxFreq = 0

        for key in freqMap:
            maxFreq = max(maxFreq, freqMap[key])
        
        slots = (maxFreq-1) * (n+1)

        for key in freqMap:
            if freqMap[key] == maxFreq:
                slots += 1

        return max(slots, len(tasks))