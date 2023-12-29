import java.util.*;

class Program {

  public static int nodeDepths(BinaryTree root) {
    TreeInfo info = new TreeInfo(0);
		int depth=0;
		calculateSum(root, info, depth);
    return info.currentSum;
  }
	public static void calculateSum(BinaryTree node, TreeInfo info, int depth){
		if(node == null) return;
		info.currentSum += depth;
		
		calculateSum(node.left, info, depth+1);
		calculateSum(node.right, info, depth+1);
		
	}
	
	static class TreeInfo{
		public int currentSum;
		
		public TreeInfo(int currentSum){
			this.currentSum = currentSum;
		}
	}

  static class BinaryTree {
    int value;
    BinaryTree left;
    BinaryTree right;

    public BinaryTree(int value) {
      this.value = value;
      left = null;
      right = null;
    }
  }
}

