# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.dfs(root, 0, [], result, targetSum, set())
        return result

    def dfs(self, node, currSum, path, result, targetSum, visited):
        if not node:
            return
        
        if not node.left and not node.right and currSum + node.val == targetSum:
            result.append(path + [node.val])
            return

        #explore left subtree
        self.dfs(node.left, currSum + node.val, path + [node.val], result, targetSum, visited)

        # explore right subtree
        self.dfs(node.right, currSum + node.val, path + [node.val], result, targetSum, visited)

        

    


        