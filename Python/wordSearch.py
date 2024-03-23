class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.wordExists(i,j,board,word,0,set()):
                    return True
        
        return False
        
    def wordExists(self, i, j, board, word, idx, visited):
        # if we have found the word
        if idx == len(word):
            return True
        
        # if we go out of bounds, there is no way to find the word
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or (i,j) in visited:
            return False
        
        # if we found the first character of the word at current pos
        if board[i][j] != word[idx]:
            return False

        # mark current cell as visited
        visited.add((i,j))

        dx, dy = [0,0,1,-1], [1,-1,0,0]
        
        # check if the remaining word exists if we start from any neighbour
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]

            if self.wordExists(x,y,board,word,idx+1,visited.copy()):
                return True

        visited.remove((i,j))
        return False

