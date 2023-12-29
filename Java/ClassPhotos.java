import java.util.*;

class Program {

  public boolean classPhotos(
    ArrayList<Integer> redShirtHeights, ArrayList<Integer> blueShirtHeights) {
   
		Collections.sort(redShirtHeights);
		Collections.sort(blueShirtHeights);
		
		if(redShirtHeights.get(0)< blueShirtHeights.get(0) ){
			//blue shirt people in the back row
			for(int i=1; i<redShirtHeights.size(); i++){
				if(redShirtHeights.get(i) >blueShirtHeights.get(i) ) return false;
			}
		}
		
		else if(blueShirtHeights.get(0) <redShirtHeights.get(0)){
			//red shirt people in back row
			for(int j=1; j<blueShirtHeights.size(); j++){
				if(blueShirtHeights.get(j)>redShirtHeights.get(j)) return false;
			}
		}
		else if(blueShirtHeights.get(0)==redShirtHeights.get(0)) return false;
		
    return true;
  }
}

