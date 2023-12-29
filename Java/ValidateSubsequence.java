import java.util.*;

class Program {
  public static boolean isValidSubsequence(List<Integer> array, List<Integer> sequence) {
    int p1=0,p2=0;
		
		//Iterative aproach, O(N)T, O(1) S
		
		while(p1<array.size() && p2<sequence.size()){
			if(array.get(p1) == sequence.get(p2)){
				if(p2==sequence.size()-1){
					return true;
				}
				else{
					p1++;
					p2++;
				}
			}
			else{
				p1++;
			}
		}
		
    return false;
  }
}

