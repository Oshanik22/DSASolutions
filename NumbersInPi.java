import java.util.*;

class Program {
  public static int numbersInPi(String pi, String[] numbers) {
    HashSet<String> fav = new HashSet<String>();
		for( String number : numbers) fav.add(number);
		HashMap<String, Integer> memoise = new HashMap<String, Integer>();
		int result = numbersInPi(pi, memoise, fav);
    return result==Integer.MAX_VALUE? -1 : result;
  }
	
	public static int numbersInPi(String num, HashMap<String, Integer> memoise, HashSet<String> fav){
		if(fav.contains(num)) return 0;
		if(memoise.containsKey(num)) return memoise.get(num);
		int min = Integer.MAX_VALUE;
		for(int idx=1; idx<=num.length(); idx++){
			String currentSubstring = num.substring(0,idx);
			if(fav.contains(currentSubstring)){
				int noOfSpaces = numbersInPi(num.substring(idx), memoise, fav);
				if(noOfSpaces == Integer.MAX_VALUE){
					min = Math.min(noOfSpaces, min);
				}else{
					min = Math.min(noOfSpaces+1, min);
				}
			}
		}
		return min;
	}
}



