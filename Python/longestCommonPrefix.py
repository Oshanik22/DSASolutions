class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minStr = min(strs)
        maxStr = max(strs)
        i=0
        while i < len(minStr):
            if minStr[i] != maxStr[i]:
                return minStr[:i]
            i+=1
            
        return minStr