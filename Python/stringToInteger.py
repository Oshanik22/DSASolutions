class Solution:

    def myAtoi(self, s):
        res = 0
        sign = 1
        digits = "0123456789"
        s = s.strip()

        if s and (s[0] == "-" or s[0] == "+"):
            if s[0] == "-":
                sign = -1
                s = s[1:]
            elif s[0] == "+": 
                sign = +1
                s = s[1:]
            

        for char in s:
            if char in digits:
                res = res * 10 + int(char)
            else:
                break
        res *= sign
        IntMax = 2**31 - 1
        IntMin = -2**31
        res = max(IntMin, min(IntMax, res))
        return res