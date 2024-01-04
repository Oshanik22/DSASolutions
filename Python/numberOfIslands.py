class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # go through the matrix, if you find a 1, that means its part of an unexplored island, so explore it, and mark every explored node as 2
        # increment counter
        n, m, count = len(grid), len(grid[0]), 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.explore(grid, i, j, n, m)
                    count += 1

        return count
    
    def explore(self, grid, i, j, n, m):
        # if out of bounds or if already visited or if water, then skip
        if not 0<=i< n or not 0<=j<m or grid[i][j] in ['0', '2']:
            return
        
        # mark as visited
        grid[i][j] = '2'

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for dr, dc in directions:
            self.explore(grid, i+dr, j+dc, n, m)
        
        return
