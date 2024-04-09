class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # figure out which rows and cols to be set to 0
        zeroRows = set()
        zeroCols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)

        # set these to 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zeroRows or j in zeroCols:
                    matrix[i][j] = 0

        