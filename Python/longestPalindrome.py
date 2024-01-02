class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        result = 0
        oddFound = False
        for char, count in freq.items():
            pairs = count//2
            result += pairs * 2
            if count % 2 == 1:
                oddFound = 1
        
        
        return result + 1 if oddFound else result