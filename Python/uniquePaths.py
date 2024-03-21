class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memoise = [[0 for i in range(n)] for i in range(m)]
        return self.uniquePathsHelper(0,0,m,n,memoise)

    def uniquePathsHelper(self, i, j, m, n, memoise):
        if i>=m or j>=n:
            return 0
        
        if i==m-1 and j==n-1:
            return 1

        if memoise[i][j]:
            return memoise[i][j]

        ways = 0
        ways += self.uniquePathsHelper(i+1,j,m,n,memoise)
        ways += self.uniquePathsHelper(i,j+1,m,n,memoise)

        memoise[i][j] = ways

        return ways