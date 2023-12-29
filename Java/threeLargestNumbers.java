import java.util.*;

class Program {
  public static int[] findThreeLargestNumbers(int[] array) {
    int[] result = {Integer.MIN_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE};
		for(int i : array){
			if(i>result[2]){
				result[0]=result[1];
				result[1]=result[2];
				result[2]=i;
			}
			else if(i>result[1]){
				result[0]=result[1];
				result[1]=i;
			}
			else if(i>result[0]){
				result[0]=i;
			}
		}
		
    return result;
  }
}

