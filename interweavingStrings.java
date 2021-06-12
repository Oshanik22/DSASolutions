import java.util.*;

class Program {
  public static boolean interweavingStrings(String one, String two, String three) {
		if(three.length() != one.length() + two.length()) return false;
		boolean[][] memoise = new boolean[one.length() + 1][two.length()+1];
		return interweavingStrings(one,two,three,0,0, memoise);
  }
	public static boolean interweavingStrings(String one, String two, String three, int p1, int p2, boolean[][] memoise) {
		if(memoise[p1][p2])return memoise[p1][p2];
		int p3 = p1+p2;
		if(p3 == three.length()) return true;
		if(p1<one.length() && one.charAt(p1)==three.charAt(p3)){
			if(interweavingStrings(one,two,three,p1+1,p2, memoise)){
				memoise[p1][p2] = true;
				return memoise[p1][p2];
			}
		}
		if(p2<two.length() && two.charAt(p2)==three.charAt(p3)){
			memoise[p1][p2] = (interweavingStrings(one,two,three,p1,p2+1, memoise));
			return memoise[p1][p2];
		}
		memoise[p1][p2] = false;
		return memoise[p1][p2];
		
	}
}

