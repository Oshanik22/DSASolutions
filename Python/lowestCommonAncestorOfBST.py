# So basically, you need to leverage the property of a bst that is, 
# 1. all the elements in the left subtree will be smaller than elemtns of the right subtree
# 2. if a node has p smaller than it and q larger than it, than it has to be the LCA of the two because this is the point from which the two nodes start to be on separate subtrees
# 3. And for every node above this one, both p and q will either be smaller than it or larger than it, but both will have similar behaviour, if they had different behaviour, they would have ended up on different subtrees.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
