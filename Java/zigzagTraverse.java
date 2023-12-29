import java.util.*;

class Program {
  public static List<Integer> zigzagTraverse(List<List<Integer>> array) {
    List<Integer> result = new ArrayList<Integer>();
		int pairSum = 0;
		boolean flipped = true;
		int n = array.size();
		int m = array.get(0).size();
		while(pairSum<n+m-1){
			List<Integer[]> cords = calculateCords(pairSum, n, m, flipped);
			for(Integer[] cord : cords){
				result.add(array.get(cord[0]).get(cord[1]));
			}
			pairSum++;
			flipped = !flipped;
		}
    return result;
  }
	
	public static List<Integer> calculateCords(int pairSum, int n, int m, boolean flipped){
		int a = pairSum%m;
		
	}
}

