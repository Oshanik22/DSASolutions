class Solution {

    boolean isSame=true;
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if((p==null && q!= null) ||(p!=null && q== null)) return false;
        
        if(p!=null&&q!=null){
            if(p.val!=q.val) return false;
            isSame = isSameTree(p.left, q.left);
            isSame = isSameTree(p.right, q.right);
        }
        else{
            return isSame;
        }
        
    return isSame;
    }
}
