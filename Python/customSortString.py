class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        result = ""

        for char in order:
            while char in freq and freq[char] > 0:
                result += char
                freq[char] -= 1
            
        for key in freq:
            while freq[key] > 0:
                result += key
                freq[key] -= 1

        return result