# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.calculateHeightAndUpdateDiameter(root)
        return self.diameter-1 if self.diameter else 0
    
    def calculateHeightAndUpdateDiameter(self, root):
        #this function updates the diameter global variable and returns height of this tree
        if not root:
            return 0
        
        leftHeight = self.calculateHeightAndUpdateDiameter(root.left)
        rightHeight = self.calculateHeightAndUpdateDiameter(root.right)

        currHeight = max(leftHeight, rightHeight) + 1
        currDiameter = leftHeight + rightHeight + 1
        self.diameter = max(currDiameter, self.diameter)

        return currHeight
    