import java.util.*;

class Program {

  public ArrayList<ArrayList<Integer>> solveSudoku(ArrayList<ArrayList<Integer>> board) {
    solvePartialSudoku(0,0,board);
    return board;
  }
	public static boolean solvePartialSudoku(int row, int col, ArrayList<ArrayList<Integer>>board){
		if(col == board.get(row).size()){
			col = 0;
			row++;
			if(row == board.size()) return true;
		}
		
		if(board.get(row).get(col)==0){
			return tryDigits(row, col, board);
		}
		return solvePartialSudoku(row, col+1, board);
	}
	public static boolean tryDigits(int row, int col, ArrayList<ArrayList<Integer>> board){
		for(int digit=1; digit<10; digit++){
			if(isValidAtPosition(digit, row, col, board)){
				board.get(row).set(col, digit);
				if(solvePartialSudoku(row, col+1, board)) return true;
			}
		}
		board.get(row).set(col, 0);
		return false;
	}
	public static boolean isValidAtPosition(int value, int row, int col, ArrayList<ArrayList<Integer>> board){
		boolean isValidRow = !board.get(row).contains(value);
		boolean isValidCol = true;
		for(int i=0; i<board.size(); i++){
			if(board.get(i).get(col)==value) return false;
		}
		if(!isValidRow || !isValidCol) return false;
		
		int subMatrixRowIdx = (row/3)*3;
		int subMatrixColIdx = (col/3)*3;
		for(int i=subMatrixRowIdx; i<subMatrixRowIdx+3; i++){
			for(int j=subMatrixColIdx; j<subMatrixColIdx+3; j++){
				if(board.get(i).get(j)==value) return false;
			}
		}
		return true;
	}
}
