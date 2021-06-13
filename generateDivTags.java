import java.util.*;

class Program {

  public ArrayList<String> generateDivTags(int numberOfTags) {
		ArrayList<String> result = new ArrayList<String>();
		generate(new StringBuilder(), numberOfTags, numberOfTags, 0, 0, result);
    return result;
  }
	public static void generate(StringBuilder sb, int opLeft, int closingLeft, int opUsed, int closingUsed, ArrayList<String> result){
		if(opLeft == 0 && closingLeft==0){
			result.add(sb.toString());
			return;
		}
		if(closingUsed>opUsed) return;
		if(opLeft>0){
			StringBuilder newSb = new StringBuilder(sb);
			newSb.append("<div>");
			generate(newSb, opLeft-1, closingLeft, opUsed+1, closingUsed, result);
		}
		if(closingLeft>0){
			StringBuilder newSb = new StringBuilder(sb);
			newSb.append("</div>");
			generate(newSb, opLeft, closingLeft-1, opUsed, closingUsed+1, result);
		}
		
	}
}
