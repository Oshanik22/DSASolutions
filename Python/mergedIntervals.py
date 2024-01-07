class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        result = []
        intervals.sort()
        currInterval = intervals[0]

        for i in range(1, len(intervals)):
            nextInterval = intervals[i]
            if currInterval[1] >= nextInterval[0]:
                currInterval[0] = min(currInterval[0], nextInterval[0])
                currInterval[1] = max(currInterval[1], nextInterval[1])
            
            else:
                result.append(currInterval)
                currInterval = nextInterval

        result.append(currInterval)
        return result