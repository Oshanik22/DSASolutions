import java.util.*;

class Program {
	//O(n^2)|O(n)
  public static List<Integer> longestIncreasingSubsequence(int[] array) {
    int[] lengths = new int[array.length];
		int[] indices = new int[array.length];
		Arrays.fill(lengths, 1);
		Arrays.fill(indices, -1);
		int longestSubseqIdx = calculateLengths(lengths, indices, array);
		ArrayList<Integer> result = getLongestSubsequence(array, lengths, indices, longestSubseqIdx);
		return result;
  }
	
	public static int calculateLengths(int[] lengths, int[] indices, int[] array){
		int maxLengthIdx = 0;
		for(int i=0; i<lengths.length; i++){
			int maxLength = 1; int idx = i;
			for(int j=0; j<i; j++){
				if(array[j]<array[i]){
					if(lengths[j]+1 > lengths[i]){
						maxLength = lengths[j]+1;
						lengths[i] = maxLength;
						indices[i] = j;
					} 
				}
			}
			if(lengths[i]>lengths[maxLengthIdx]) maxLengthIdx = i;
		}
		return maxLengthIdx;
	}
	
	public static ArrayList<Integer> getLongestSubsequence(int[] array, int[] lengths, int[] indices, int idx){
		ArrayList<Integer> result = new ArrayList<Integer>();
		while(idx!= -1){
			result.add(array[idx]);
			idx = indices[idx];
		}
		Collections.reverse(result);
		return result;
	}
}
