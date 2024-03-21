class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        freq = {}
        result = ""

        # create frequency map
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        #remove 1 to be placed at the end so that the number is odd
        freq['1'] -= 1

        #Put all the 1s at the front to maximise the number
        for i in range(freq['1']):
            result += '1'

        # Put all the 0s now
        if '0' in freq:
            for i in range(freq['0']):
                result += '0'

        # add the trailing 1 to make the number odd
        result += '1'

        return result 