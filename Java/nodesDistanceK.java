import java.util.*;

class Program {
  // This is an input class. Do not edit.
  static class BinaryTree {
    public int value;
    public BinaryTree left = null;
    public BinaryTree right = null;

    public BinaryTree(int value) {
      this.value = value;
    }
  }
	static class Pair<U,V>{
		public final U first;
		public final V second;
		private Pair(U first, V second){
			this.first = first;
			this.second = second;
		}
	}

  public ArrayList<Integer> findNodesDistanceK(BinaryTree tree, int target, int k) {
    HashMap<Integer, BinaryTree> parents = new HashMap<Integer, BinaryTree>();
		HashSet<Integer> visited = new HashSet<Integer>();
		getParents(tree, null, parents);
		BinaryTree node = getNodeFromValue(target, parents, tree);
		Queue<Pair<BinaryTree, Integer>> queue = new LinkedList<Pair<BinaryTree, Integer>>();
		queue.add(new Pair<BinaryTree, Integer>(node, 0));
		visited.add(target);
		while(!queue.isEmpty()){
			Pair<BinaryTree, Integer> currentPair = queue.poll();
			BinaryTree currentNode = currentPair.first;
			int currentDist = currentPair.second;
			if(currentDist == k){
				ArrayList<Integer> result = new ArrayList<Integer>();
				for(Pair<BinaryTree, Integer> pair : queue){
					result.add(pair.first.value);
				}
				result.add(currentNode.value);
				return result;
			}
			List<BinaryTree> connectedNodes = new ArrayList<BinaryTree>();
			connectedNodes.add(currentNode.left);
			connectedNodes.add(currentNode.right);
			connectedNodes.add(parents.get(currentNode.value));
			
			for(BinaryTree nextNode : connectedNodes){
				if(nextNode == null) continue;
				if(visited.contains(nextNode.value)) continue;
				visited.add(nextNode.value);
				queue.add(new Pair<BinaryTree, Integer>(nextNode, currentDist+1));
			}
		}
		
		return new ArrayList<Integer>();
  }
	public static void getParents(BinaryTree node, BinaryTree parent, HashMap<Integer, BinaryTree> parents){
		if(node != null){
			parents.put(node.value, parent);
			getParents(node.left, node, parents);
			getParents(node.right, node, parents);
		}
	}
	public static BinaryTree getNodeFromValue(int current, HashMap<Integer, BinaryTree> parents, BinaryTree tree){
		if(tree.value == current) return tree;
		BinaryTree parent = parents.get(current);
		if(parent.left != null && parent.left.value == current){
			return parent.left;
		}
		return parent.right;
	}
}

