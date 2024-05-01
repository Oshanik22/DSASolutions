class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        if k > len(cardPoints):
            return sum(cardPoints)

        # calculate lsum
        lsum = 0
        left = 0
        while left < k:
            lsum += cardPoints[left]
            left += 1

        if left==len(cardPoints):
            return lsum

        maxSum = lsum
        right = len(cardPoints)-1
        left = k-1
        rsum = 0

        # shrink left window, expand right window, keep track of max
        while left >= 0 and right >= 0:
            lsum -= cardPoints[left]
            left -= 1

            rsum += cardPoints[right]
            right -= 1

            maxSum = max(maxSum, lsum + rsum)

        # return max 

        return maxSum