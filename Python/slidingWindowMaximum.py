class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxElements = deque()
        left = 0
        right = 0
        result = []

        while right < len(nums):
            while maxElements and nums[right] > maxElements[-1]:
                maxElements.pop()
            
            maxElements.append(nums[right])

            winSize = right-left + 1

            if winSize < k:
                right += 1

            if winSize == k:
                result.append(maxElements[0])

                if maxElements[0] == nums[left]:
                    maxElements.popleft()
                left+= 1
                right+= 1
        
        return result
