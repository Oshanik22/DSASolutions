# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, -math.inf, math.inf)

    def isValidBSTHelper(self, node, minVal, maxVal):
        if not node:
            return True
        
        if minVal < node.val < maxVal:
            isLeftValid = self.isValidBSTHelper(node.left, minVal, node.val)
            isRightValid = self.isValidBSTHelper(node.right, node.val, maxVal)

            return isLeftValid and isRightValid
        
        return False