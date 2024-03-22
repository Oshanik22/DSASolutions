class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        combinations = {2:["a","b","c"], 3:["d","e","f"], 4:["g","h","i"], 5:["j","k","l"], 6:["m","n","o"], 7:["p","q","r","s"], 8:["t", "u", "v"], 9:["w", "x", "y", "z"]}
        self.findCombinations(digits,combinations,result, "")
        return result

    def findCombinations(self, digits, combinations, result, currCombination):
        if not digits:
            result.append(currCombination)
            return
        
        firstNum = int(digits[0])
        for letter in combinations[firstNum]:
            self.findCombinations(digits[1:], combinations, result, currCombination+letter)

        


