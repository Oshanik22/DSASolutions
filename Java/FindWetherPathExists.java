class Solution
{
    //Function to find whether a path exists from the source to destination.
    public boolean is_Possible(int[][] grid)
    {
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                if(grid[i][j]==1){
                    return isPath(i,j,grid);
                }
            }
        }
        return true;
    }

    public boolean isPath(int i, int j, int[][] grid){
        boolean[][] visited = new boolean[grid.length][grid.length];

        Queue<int[]> cells= new LinkedList<int[]>();
        cells.offer(new int[]{i,j});

        while(!cells.isEmpty()){
            int[] cell = cells.poll();
            int x = cell[0], y = cell[1];

            //If not visited, mark as visited, else skip it
            if(visited[x][y]) continue;
            visited[x][y] = true;

            //If we have reached destination
            if(grid[x][y]==2) return true;


            //Visiting top, bottom, left, right
            int[] xDir = new int[]{0,0,1,-1};
            int[] yDir = new int[]{1,-1,0,0};

            for(int k=0; k<4; k++){
                int X = x + xDir[k];
                int Y = y + yDir[k];

                if(isValid(X,Y, grid)){
                    cells.offer(new int[]{X,Y});
                }
            }
        }

        return false;
    }

    public boolean isValid(int i, int j, int[][] grid){
      if(i<0 || j<0 || i>=grid.length || j>=grid[0].length || grid[i][j] == 0) return false;
      return true;

    }
}
