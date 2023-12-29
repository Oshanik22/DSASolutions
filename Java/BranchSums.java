import java.util.*;

class Program {
  // This is the class of the input root. Do not edit it.
  public static class BinaryTree {
    int value;
    BinaryTree left;
    BinaryTree right;

    BinaryTree(int value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }

  public static List<Integer> branchSums(BinaryTree root) {
    List<Integer> result = new ArrayList<Integer>();
		branchSum(root, 0, result);
    return result;
  }
	
	public static void branchSum(BinaryTree root, int prevSum, List<Integer> list){
		if(root == null) return ;
		
		int newSum = prevSum + root.value;
		if(root.left == null && root.right==null){
			//if leaf node
			list.add(newSum);
			return;
		}
		
		branchSum(root.left, newSum, list);
		branchSum(root.right, newSum, list);
		
	}
}

