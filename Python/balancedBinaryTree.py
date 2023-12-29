# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, height = self.isBalAndCalcHeight(root)
        return balanced
    
    def isBalAndCalcHeight(self, root):
        if not root:
            return (True, 0)
        
        leftBalanced, leftHeight = self.isBalAndCalcHeight(root.left)
        rightBalanced, rightHeight = self.isBalAndCalcHeight(root.right)

        balanced = leftBalanced and rightBalanced and abs(leftHeight-rightHeight) <= 1
        height = 1 + max(leftHeight, rightHeight)

        return (balanced, height)