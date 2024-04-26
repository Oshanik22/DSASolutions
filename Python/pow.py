class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==-1:
            return 1/x
        if n==0:
            return 1
        if n==1:
            return x

        halfPower = self.myPow(x, n//2)
        
        if n%2:
            return x * halfPower * halfPower

        else:
            return halfPower * halfPower