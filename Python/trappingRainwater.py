class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        maxLeft = height[0]
        maxRight = height[-1]

        left = 0
        right = len(height)-1
        water = 0
        
        while (left < right):
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])

            if maxLeft < maxRight:
                water += max(0, maxLeft-height[left])
                left += 1
            
            else:
                water += max(0, maxRight-height[right])
                right -= 1

        return water