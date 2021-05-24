import java.util.*;
import java.lang.*;
class Program {

  public int[] sortedSquaredArray(int[] array) {
    int l=0;
		int r=array.length-1;
		int element1,element2;
		
		int[] result = new int[array.length];
		int p=result.length-1;
		while(l<=r){
			
			element1=Math.abs(array[l]);
			element2=Math.abs(array[r]);
			
			if(element1>element2){
				result[p]=array[l]*array[l];
				p--;
				l++;
			}
			else if (element2>element1){
				result[p]=array[r]*array[r];
				p--;
				r--;
			}
			else if(element1==element2){
				result[p]=array[r]*array[r];
				p--;
				r--;
			}
		}
		
    return result;
  }
}

