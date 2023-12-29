import java.util.*;

class Program {

  public int maximizeExpression(int[] array) {
		if(array.length<4) return 0;
    int[] sum1 = new int[array.length];
		int currentMax = Integer.MIN_VALUE;
		
		//every index i in sum1 represents the max value of 'a' till that index
		sum1[0] = array[0];
		for(int i=1; i<sum1.length; i++){
			sum1[i] = Math.max(sum1[i-1], array[i]);
		}
		
		int[] sum2 = new int[array.length];
		
		//every index in sum2 represents the max 'a-b' till that index
		sum2[0] = 0;
		for(int i=1; i<array.length; i++){
			sum2[i] = Math.max(sum1[i-1]-array[i], currentMax);
			currentMax = sum2[i];
		}
		currentMax = Integer.MIN_VALUE;
		//a-b+c
		sum1[0] = 0; sum1[1] = 0;
		for(int i=2; i<array.length; i++){
			sum1[i] = Math.max(sum2[i-1] + array[i], currentMax);
			currentMax = sum1[i];
		}
		
		currentMax = Integer.MIN_VALUE;
		//a-b+c-d
		sum2[1]=0; sum2[2]=0;
		for(int i=3; i<array.length; i++){
			sum2[i] = sum1[i-1]-array[i];
			currentMax = Math.max(currentMax, sum2[i]);
		}
		
    return currentMax;
  }
}

