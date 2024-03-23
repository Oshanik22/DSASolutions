class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        sCount = [0 for _ in range(26)] 
        pCount = [0 for _ in range(26)]
        result = []

        for i in range(len(p)):
            sCount[ord(s[i])-ord('a')] += 1
            pCount[ord(p[i])-ord('a')] += 1

        # i points to 1 idx before the start of the window
        for i in range(len(s)-len(p)):
            # if the window next to the previous i was a valid window, add it to the result
            if sCount == pCount:
                result.append(i)

            #update counts
            sCount[ord(s[i+len(p)])-ord('a')] += 1
            sCount[ord(s[i])-ord('a')] -= 1

        # check for the last window
        if sCount == pCount:
            result.append(len(s)-len(p))

        return result
            