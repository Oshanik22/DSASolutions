class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        p1,p2 = len(num1)-1,len(num2)-1
        carry = 0

        while p1>=0 or p2>=0 or carry:
            n1 = int(num1[p1]) if p1>=0 else 0
            n2 = int(num2[p2]) if p2>=0 else 0

            total = n1 + n2 + carry
            carry = total // 10
            result += str(total % 10)
            p1 -= 1
            p2 -= 1

        return result[::-1]