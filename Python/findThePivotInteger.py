class Solution:
    def pivotInteger(self, n: int) -> int:
        total = (n*(n+1))/2
        print("total: " + str(total))
        currSum = 0
        for i in range(1,n+1):
            currSum += i
            print("currrSum: " + str(currSum) + " i: " + str(i))
            if currSum == (total-currSum)+i:
                return i
        
        return -1
        