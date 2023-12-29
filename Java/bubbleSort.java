import java.util.*;

class Program {
  public static int[] bubbleSort(int[] array) {
    
		int iterateUpto = array.length-1;
		int temp;
		boolean didSwap=false;
		while(true){
			didSwap=false;
			for(int i =0; i<iterateUpto; i++){
				if(array[i]>array[i+1]){
					temp = array[i+1];
					array[i+1]=array[i];
					array[i]=temp;
					didSwap=true;
				}	
			}
			iterateUpto--;
			if(!didSwap){
				break;
			}
		}
    return array;
  }
}

