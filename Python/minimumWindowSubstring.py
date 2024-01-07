class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""

        countT = Counter(t)
        freq = {}
        matches = 0
        reqMatches = len(countT)

        result, resultWindow = math.inf, [-1,-1]

        i = 0
        j = -1

        while j<len(s):
            if matches < reqMatches:
                # expand
                j+= 1
                if j < len(s):
                    freq[s[j]] = 1 + freq.get(s[j], 0)
                    if s[j] in countT and freq[s[j]] == countT[s[j]]:
                        matches += 1
                
            else:
                # Update result
                windowSize = j-i+1
                if windowSize < result:
                    result = windowSize
                    resultWindow[0], resultWindow[1] = i, j

                # shrink 
                if s[i] in freq:
                    freq[s[i]] -= 1

                # if we have lost a match
                if s[i] in countT and freq[s[i]] == countT[s[i]] - 1:
                    matches -= 1
                
                i += 1
        l,r = resultWindow
        return s[l:r+1] if result != math.inf else ""