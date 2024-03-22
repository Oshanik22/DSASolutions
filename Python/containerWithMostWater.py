class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater, left, right = 0, 0, len(height)-1

        while left < right:
            water = (right-left) * (min(height[left], height[right]))
            maxWater = max(maxWater, water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater
        