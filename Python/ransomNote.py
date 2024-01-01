class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = Counter(magazine)
        
        for letter in ransomNote:
            if letter not in freq or not freq[letter]:
                return False
            freq[letter] -= 1

        return True