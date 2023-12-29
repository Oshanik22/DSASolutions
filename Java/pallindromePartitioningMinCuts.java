import java.util.*;

class Program {
  public static int palindromePartitioningMinCuts(String str) {
    int[] memoise = new int[str.length()];
    return calculateCuts(0, str, memoise);
  }
	
	public static int calculateCuts(int start, String string, int[] memoise){
		if(memoise[start]>0) return memoise[start];
		if(isPalindrome(start, string.length()-1, string)){
			return 0;
		}
		int minCuts = Integer.MAX_VALUE;
		for(int end=string.length()-1; end>=start; end--){
			if(isPalindrome(start, end, string)){
				int noOfCuts = calculateCuts(end+1, string, memoise);
				if(noOfCuts != Integer.MAX_VALUE){
					minCuts = Math.min(noOfCuts+1, minCuts);
				}
			}
		}
		memoise[start] = minCuts;
		return minCuts;
	}
	
	public static boolean isPalindrome(int start, int end, String string){
		while(start < end){
			if(string.charAt(start)!=string.charAt(end)) return false;
			start++;
			end--;
		}
		return true;
	}
}
