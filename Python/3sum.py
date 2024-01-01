class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1

            while j<k:
                currSum = nums[i] + nums[j] + nums[k]
                if currSum == 0:
                    triplets.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif currSum < 0:
                    j+=1
                else:
                    k-=1

        return list(triplets)