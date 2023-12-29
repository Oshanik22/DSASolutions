class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        result = []
        # for all the intervals less than the newInterval, we have to move them to a new list
        while i<len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i+=1

        # now we need to merge all intervals with our new interval
        while i<len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i+=1

        # insert new interval into the result list
        result.append(newInterval)

        # now that we are sure that all the intervals that could have been merged have been merged, the only intervals remaining are the ones that are greater than our new intervals
        while i<len(intervals):
            result.append(intervals[i])
            i+=1
        return result