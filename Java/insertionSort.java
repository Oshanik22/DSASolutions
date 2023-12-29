import java.util.*;

class Program {
  public static int[] insertionSort(int[] array) {
		int j, temp;
    for(int i=0; i<array.length; i++){
			j=i;
			while(j>0 && array[j]<array[j-1]){
				temp = array[j-1];
				array[j-1]=array[j];
				array[j]=temp;
				j--;
			}
		}
    return array;
  }
}

