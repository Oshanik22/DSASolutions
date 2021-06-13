import java.util.*;

class Program {
  public static int maxProfitWithKTransactions(int[] prices, int k) {
    if(prices.length==0) return 0;
		int[] array1 = new int[prices.length];
		int[] array2 = new int[prices.length];
		int[] current = array1;
		int[] prev = array2;
		for(int t=1; t<k+1; t++){
			int max = Integer.MIN_VALUE;
			int[] temp = prev;
			prev = current;
			current = temp;
			Arrays.fill(current, 0);
			for(int d=1; d<prices.length; d++){
				max = Math.max(max, prev[d-1] - prices[d-1]);
				current[d] = Math.max(prices[d] + max , current[d-1]);
			}
		}
    return current[prices.length-1];
  }
}
