class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastSeen = {'a':-1, 'b':-1, 'c':-1}
        count = 0

        for i in range(len(s)):
            lastSeen[s[i]] = i

            if lastSeen['a'] != -1 and lastSeen['a'] != -1 and lastSeen['c'] != -1:
                left = min(lastSeen['a'], lastSeen['b'], lastSeen['c'])
                count += left+1

        return count