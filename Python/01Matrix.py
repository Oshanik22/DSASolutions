class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n,m = len(mat), len(mat[0])
        queue = deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = n*m

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r,c = row + dr, col + dc
                if 0<=r<n and 0<=c<m and mat[r][c] > 1 + mat[row][col]:
                    queue.append((r,c))
                    mat[r][c] = 1 + mat[row][col]

        return mat

