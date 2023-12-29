import java.util.*;

class Program {
  public String runLengthEncoding(String string) {
    int runningLength=1;
		StringBuilder result = new StringBuilder();
		
		for(int i=1; i<string.length(); i++){
			char currentChar=string.charAt(i);
			char previousChar=string.charAt(i-1);
			
			if(currentChar != previousChar || runningLength==9){
				result.append(Integer.toString(runningLength));
				result.append(previousChar);
				runningLength=0;
			}
			runningLength++;
			
		}
		result.append(Integer.toString(runningLength));
		result.append(string.charAt(string.length()-1));
    return result.toString();
  }
}

