import java.util.*;

class Program {

  public int nonAttackingQueens(int n) {
    HashSet<Integer> unsafeCol = new HashSet<Integer>();
		HashSet<Integer> unsafeDiagUp = new HashSet<Integer>();
		HashSet<Integer> unsafeDiagDown = new HashSet<Integer>();
		
    return waysToPlaceQueens(0, unsafeCol, unsafeDiagUp, unsafeDiagDown, n);
  }
	
	public int waysToPlaceQueens(
		int row,
		HashSet<Integer> unsafeCol,
		HashSet<Integer> unsafeDiagUp,
		HashSet<Integer> unsafeDiagDown,
		int n){
		
		if(row == n) return 1;
		int ways = 0;
		for(int col=0; col<n; col++){
			if(isSafe(row, col, unsafeCol, unsafeDiagUp, unsafeDiagDown)){
				placeQueen(row,col, unsafeCol, unsafeDiagUp, unsafeDiagDown);
				ways += waysToPlaceQueens(row + 1, unsafeCol, unsafeDiagUp, unsafeDiagDown, n);
				removeQueen(row,col, unsafeCol, unsafeDiagUp, unsafeDiagDown);
			}
		}
		return ways;
	}
	
	public static boolean isSafe(int row, int col, HashSet<Integer> unsafeCol, HashSet<Integer> unsafeDiagUp, HashSet<Integer> unsafeDiagDown){
		if(unsafeCol.contains(col)) return false;
		if(unsafeDiagUp.contains(row+col)) return false;
		if(unsafeDiagDown.contains(row-col)) return false;
		return true;
	}
	
	public static void placeQueen(int row, int col, HashSet<Integer> unsafeCol, HashSet<Integer> unsafeDiagUp, HashSet<Integer> unsafeDiagDown){
		unsafeCol.add(col);
		unsafeDiagUp.add(row+col);
		unsafeDiagDown.add(row-col);
	} 
	
	public static void removeQueen(int row, int col, HashSet<Integer> unsafeCol, HashSet<Integer> unsafeDiagUp, HashSet<Integer> unsafeDiagDown){
		unsafeCol.remove(col);
		unsafeDiagUp.remove(row+col);
		unsafeDiagDown.remove(row-col);
	}
	
}

