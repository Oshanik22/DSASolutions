import java.util.*;

class Program {
  public static boolean isPalindrome(String str) {
    
    return isPalindrome(str, 0, str.length()-1);
  }
	public static boolean isPalindrome(String str, int left, int right){
		if(left<right){
			if(str.charAt(left)==str.charAt(right) && isPalindrome(str, left+1, right-1)){
				return true;
			}
			return false;
		}
		return true;
	}
}
