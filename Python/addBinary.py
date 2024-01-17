class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        a = a[::-1]
        b = b[::-1]

        carry = 0
        i,j = 0,0
        while i<len(a) or j<len(b):
            digA = int(a[i]) if i < len(a) else 0
            digB = int(b[j]) if j < len(b) else 0
            total = digA + digB + carry
            char = str(total%2)
            result = char + result
            carry = total //2
            i += 1
            j += 1
        
        if carry:
            result = "1" + result

        return result