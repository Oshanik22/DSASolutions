import java.util.*;

class Program {
  public static int binarySearch(int[] array, int target) {
    int left=0;
		int right=array.length-1;
		int middle;
		
		while(left<=right){
			middle = (left+right)/2;
			if(array[middle]==target) return middle;
			if(array[middle]<target){
				left = middle+1;
			}else {
				right = middle-1;
			}
		}
    return -1;
  }
}

