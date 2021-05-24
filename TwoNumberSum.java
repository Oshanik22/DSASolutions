import java.util.*;

class Program {
  public static int[] twoNumberSum(int[] array, int targetSum) {
	//brute force O(n^2)T, O(1)S	
    int[] result = new int[2];
		
		for (int i=0; i<array.length; i++){
			for (int j=i+1; j<array.length; j++){
				if (array[i] + array[j] == targetSum){
					result[0]=array[i];
					result[1]=array[j];
					return result;
				}
			}
		}
		
    return new int[0];
  }
}


/*
so basically we are going to first do a brute force approcah,
in which we make all possible pairs and check if sum = targetsum

if sum==targetSum{
return the two numbers
}

if we reach end of array, return empty array

*/
