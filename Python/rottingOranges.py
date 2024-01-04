class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, n, m = 0, len(grid), len(grid[0])
        newRottenOranges = deque()
        freshOranges = 0

        # find out where rotten oranges are to start with
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    newRottenOranges.append((i,j))
                if grid[i][j] == 1:
                    freshOranges += 1

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        # while there are stil new oranges getting rotten
        while freshOranges and newRottenOranges:
            time +=1
            for i in range(len(newRottenOranges)):
                (x,y) = newRottenOranges.popleft()
                for dx, dy in directions:
                    X, Y = x + dx, y + dy
                    # if there is an infectable orange nearby, infect it
                    if 0<=X<n and 0<=Y<m and grid[X][Y] == 1:
                        grid[X][Y] = 2
                        freshOranges -= 1
                        newRottenOranges.append((X,Y))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        
        return time