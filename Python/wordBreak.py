class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        return self.isValid(words, s, {})

    def isValid(self, words, s, memoise):
        if s in words:
            return True

        print("s= " + s)
        if s in memoise:
            return memoise[s]
        
        result = False

        for i in range(1,len(s)+1):
            print("Checking for: " + s[:i])
            if s[:i] in words:
                if self.isValid(words, s[i:], memoise):
                    result = True
                    break
        
        memoise[s] = result
        return result
        
