class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.calculatePartitions([], result, s)
        return result
    
    def calculatePartitions(self, path, result, s):
        if not s:
            result.append(path)

        for i in range(len(s)):
            part1 = s[:i+1]
            if self.isPalindrome(part1):
                self.calculatePartitions(path + [part1], result, s[i+1:])

    def isPalindrome(self, s):
        return s == s[::-1]