import java.util.*;

class Program {

  public int maximumSumSubmatrix(int[][] matrix, int size) {
    int[][] sums = makeSumsMatrix(matrix);
		int max = Integer.MIN_VALUE;
		for(int i=size-1; i<matrix.length; i++){
			for(int j=size-1; j<matrix[0].length; j++){
				int current = sums[i][j];
				int left = j-size>=0? sums[i][j-size] : 0;
				int up = i-size>=0? sums[i-size][j] : 0;
				int diagonal = i-size>=0&& j-size>=0? sums[i-size][j-size] : 0;
				int currentSum = (current-up-left+diagonal);
				max = Math.max(currentSum, max);
			}
		}
    return max==Integer.MIN_VALUE? -1 : max;
  }
	
	
	public static int[][] makeSumsMatrix(int[][] matrix){
		int[][] sums = new int[matrix.length][matrix[0].length];
		sums[0][0] = matrix[0][0];
		//filling values in first row and first col
		for(int i=0; i<matrix.length; i++){
			for(int j=0; j<matrix[0].length; j++){
				if(i==0 && j!=0){
					sums[i][j] = sums[i][j-1] + matrix[i][j];
				}if(j==0 && i!=0){
					sums[i][j] = sums[i-1][j] + matrix[i][j];
				}
			}
		}
		
		//filling rest of the elements
		for(int i=1; i<matrix.length; i++){
			for(int j=1; j<matrix[0].length; j++){
				int current = matrix[i][j];
				int up = sums[i-1][j];
				int left = sums[i][j-1];
				int diagonal = sums[i-1][j-1];
				sums[i][j] = up+left+current-diagonal;
			}
		}
		
		return sums;
	}
}

/*
create aux matrix , at each point i,j it stores the sum of the submatrix that 
starts at 0,0 and ends at i,j
initialise first row and col of sum 



*/
