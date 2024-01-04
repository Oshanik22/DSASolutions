class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.checkAllCombos(0, [],result, 0, candidates, target)

        return result

    def checkAllCombos(self, curr_sum, curr_comb, result, idx, candidates, target):
        if curr_sum > target:
            return

        if curr_sum == target:
            result.append(curr_comb)
            return
        
        for i in range(idx, len(candidates)):
            self.checkAllCombos(curr_sum + candidates[i], curr_comb + [candidates[i]], result, i, candidates, target)
