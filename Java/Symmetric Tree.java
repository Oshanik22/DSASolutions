/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    public boolean isSymmetric(TreeNode root) {
        TreeNode t1=root,t2 = root;
        return isEqual(t1,t2);
    }
    public boolean isEqual(TreeNode t1, TreeNode t2){
        
        if(t1==null&&t2==null) return true;
        if(t1==null || t2==null) return false;
        
        return (t1.val==t2.val) && isEqual(t1.left, t2.right) && isEqual(t1.right, t2.left);
    }
}

/*
root - untouched
root.left.val!=root.right.val => return false

tree1 = root.left
tree2 = root.right

tree1- DLR
tree2- DRL

tree1.left = isSymmetric()


*/
