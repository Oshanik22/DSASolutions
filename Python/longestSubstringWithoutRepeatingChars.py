class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        elements = {}
        maxLength = 0
        start, end = 0,0

        for i in range(len(s)):
            if s[i] not in elements or elements[s[i]] < start:
                elements[s[i]] = i
                maxLength = max(maxLength, end-start+1)
            else:
                start = elements[s[i]] + 1
                elements[s[i]] = i
            
            end += 1
        
        return maxLength