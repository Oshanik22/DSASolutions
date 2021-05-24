import java.util.*;


class Program {

  public int tandemBicycle(int[] red, int[] blue, boolean fastest) {
		int result=0;
    Arrays.sort(red);
		Arrays.sort(blue);
		int p1,p2;
		if(fastest){
			//if we need to maximise speed
			reverseArray(red);
		}
		for(int i=0; i<red.length; i++){
				result += Math.max(red[i], blue[i]);
			}
    return result;
  }
	
	public void reverseArray(int[] array){
		int p1=0;
		int p2=array.length-1;
		while(p1<p2){
			int temp = array[p1];
			array[p1]=array[p2];
			array[p2]=temp;
			p1++;
			p2--;
		}
	}
}

