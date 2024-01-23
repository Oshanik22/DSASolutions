class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        self.maxLength = 1
        self.result = s[0]

        for i in range(1, len(s)):
            self.checkMaxPalindromeAndUpdate(i, i, s)
            self.checkMaxPalindromeAndUpdate(i-1, i, s)

        return self.result

    def checkMaxPalindromeAndUpdate(self, i,j,s):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i-=1
            j+=1
        curr = s[i+1: j]
        if len(curr) > self.maxLength:
            self.maxLength = len(curr)
            self.result = curr