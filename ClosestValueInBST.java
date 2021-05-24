import java.util.*;
import java.lang.*;

class Program {
  public static int findClosestValueInBst(BST tree, int target) {
		BST currentNode = tree;
		int closest = currentNode.value;
		int value;
    while(currentNode != null){
			value = currentNode.value;
			if(value==target){return value;}
			if(Math.abs(value-target)<Math.abs(target-closest)){
				closest = value;
			}
			if(value<target){
				currentNode = currentNode.right;
			}else if (value>target){
				currentNode = currentNode.left;
			}
		}
    return closest;
  }

  static class BST {
    public int value;
    public BST left;
    public BST right;

    public BST(int value) {
      this.value = value;
    }
  }
}


