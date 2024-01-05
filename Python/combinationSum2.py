class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.findCombinations(0, 0, [], result, candidates, target)
        return result
    
    def findCombinations(self, idx, curr_sum, curr_comb, result, candidates, target):
        if curr_sum > target:
            return
        
        if curr_sum == target:
            result.append(curr_comb)
            return
        
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue

            self.findCombinations(i+1, curr_sum + candidates[i], curr_comb + [candidates[i]], result, candidates, target)
