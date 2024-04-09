class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        result = [[1],[1,1]]

        for i in range(2,n):
            currRow = []
            prevRow = result[-1]
            currRow.append(1)
            for j in range(1,i):
                currRow.append(prevRow[j-1] + prevRow[j])

            currRow.append(1)

            result.append(currRow)

        return result