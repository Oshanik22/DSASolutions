class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low,high = max(weights), sum(weights)
        result = 1

        def daysRequired(mid):
            daysReq = 1
            curWeight = 0

            for load in weights:
                if curWeight + load > mid:
                    daysReq += 1
                    curWeight = load
                else:
                    curWeight += load
            
            return daysReq

        while low <= high:
            mid = low + ((high-low)//2)
            if daysRequired(mid) <= days:
                result = mid
                high = mid-1

            else:
                low = mid+1

        return result