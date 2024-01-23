# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append(root)
        result = []

        while queue:
            currLength = len(queue)
            for i in range(currLength):
                curr = queue.popleft()
                if not curr:
                    continue
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)

                if i == currLength-1:
                    result.append(curr.val)
        
        return result