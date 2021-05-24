import java.util.*;

class Program {
  public static int kadanesAlgorithm(int[] array) {
		//O(n)|O(1) , Kadane's algorithm
    int currentSum = 0;
		int maxSum = Integer.MIN_VALUE;
		
		for(int i : array){
			currentSum += i;
			if(currentSum>maxSum) maxSum = currentSum;
			if(currentSum<0) currentSum=0;
		}
		
    return maxSum;
  }
}

/*

currentSum = 18
maxSum = 19

[3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]
 . .  . . .  . . . . .  . . . .  . .

1. Create 2 variables currentSum and maxSum.
2. Keep on adding the numbers in the array in order,
	if currentSum>maxSum, update maxSum
	if(currentSum<0) that means no point in including numbers upto this point in our solution
	because they will only decrease the sum. The max sum that numbers upto here
	can produce is maxSum
3. reset currentSum to 0 and keep going


*/
