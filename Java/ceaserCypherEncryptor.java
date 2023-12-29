import java.util.*;

class Program {
  public static String caesarCypherEncryptor(String str, int key) {
    int newKey = key%26;
		char[] result= new char[str.length()];
		for(int i=0; i<str.length(); i++){
			result[i] = getNewChar(str.charAt(i), newKey);
		}
    return new String(result);
  }
	
	public static char getNewChar(char current, int key){
		int newChar = current + key;
		if(newChar>122) return (char) (96+(newChar%122));
		return (char) newChar;
	}
}

