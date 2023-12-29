import java.util.*;

class Program {

  public int firstNonRepeatingCharacter(String string) {
    HashMap<Character, Integer> map = new HashMap<Character, Integer>();
		for(int i=0; i<string.length(); i++){
			Character c = string.charAt(i);
			map.put(c, map.getOrDefault(c,0)+1);
		}
		for(int j=0; j<string.length(); j++){
			Character c = string.charAt(j);
			if(map.get(c)==1) return j;
		}
    return -1;
  }
}

