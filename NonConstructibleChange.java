import java.util.*;

class Program {

  public int nonConstructibleChange(int[] coins) {
    int min_change=0;
		
		Arrays.sort(coins);
		for(int i : coins){
			if(i > min_change+1){
				return min_change+1;
			}
			min_change += i;
		}
		
    return min_change+1;
  }
}

