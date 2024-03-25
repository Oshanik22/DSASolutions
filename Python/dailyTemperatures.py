class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackIdx = stack.pop(-1)
                result[stackIdx] = (i-stackIdx)
            
            stack.append((temp,i))
        
        return result