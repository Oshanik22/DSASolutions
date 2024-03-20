class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:            
        neg = 0
        pos = 0

        while pos < len(nums) and nums[pos] < 0:
            pos += 1

        neg = pos-1

        result = []
        while pos < len(nums) and neg >= 0:
            posSquare = nums[pos] * nums[pos]
            negSquare = nums[neg] * nums[neg]

            if posSquare < negSquare:
                result.append(posSquare)
                pos += 1
            
            else:
                result.append(negSquare)
                neg -= 1

        while pos < len(nums):
            result.append(nums[pos] * nums[pos])
            pos += 1
        
        while neg >= 0:
            result.append(nums[neg] * nums[neg])
            neg -= 1

        return result

        