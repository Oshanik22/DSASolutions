import java.util.*;

class Program {

  public int minimumWaitingTime(int[] queries) {
    Arrays.sort(queries);
		
		int totalTimeWaited=0;
		
		for(int i=0; i<queries.length; i++){
			totalTimeWaited += (queries.length-1-i)*queries[i];
		}
		
    return totalTimeWaited;
  }
}

