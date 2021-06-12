import java.util.*;

class Program {
  // Tip: You can use `element instanceof ArrayList` to check whether an item
  // is an array or an integer.
  public static int productSum(List<Object> array) {
    
    return productSum(array, 1);
  }
	public static int productSum(List<Object> array, int multiplier){
		int sum=0;
		
		for (Object i : array){
			if(i instanceof ArrayList){
				sum += productSum((ArrayList<Object>) i, multiplier+1);
			}else{
				sum += (int) i;
			}
		}
		return sum*multiplier;
	}
}

