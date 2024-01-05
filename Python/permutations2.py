class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.findPerm([], result, Counter(nums), len(nums))
        return result

    def findPerm(self, curr_comb, result, counter, n):
        if len(curr_comb) == n:
            result.append(curr_comb)
            return
        
        for i in counter:
            if counter[i]:
                counter[i] -= 1
                self.findPerm(curr_comb + [i], result, counter, n)
                counter[i] += 1