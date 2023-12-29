import java.util.*;

class Program {
  public static int[] selectionSort(int[] array) {
    int startIdx=0;
		int smallestIdx;
		int temp;
		while(startIdx<array.length-1){
			smallestIdx=startIdx;
			for(int i=startIdx; i<array.length; i++){
				if(array[i]<array[smallestIdx]){
					smallestIdx=i;
				}
			}
			if(smallestIdx != startIdx){
				//swap
				temp = array[smallestIdx];
				array[smallestIdx]=array[startIdx];
				array[startIdx]=temp;
			}
			startIdx++;
		}
    return array;
  }
}

