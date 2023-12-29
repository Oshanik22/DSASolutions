import java.util.*;

class Program {

  public boolean generateDocument(String characters, String document) {
    HashMap<Character, Integer> map = new HashMap<Character, Integer>();
		for(int i=0; i<characters.length(); i++){
			Character c= characters.charAt(i);
			map.put(c, map.getOrDefault(c,0)+1);
		}
		
		for(int j=0; j<document.length(); j++){
			Character d = document.charAt(j);
			if(!map.containsKey(d) || map.get(d)==0){
				return false;
			}
			map.put(d,map.get(d)-1);
		}
    return true;
  }
}

