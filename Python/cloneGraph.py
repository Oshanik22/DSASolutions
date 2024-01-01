"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        newNodes = {}
        self.cloneGraph(node, newNodes)
        return newNodes[node]
    
    def cloneGraph(self, root, newNodes):
        queue = deque([root])
        newNodes[root] = Node(root.val, [])

        while queue:
            node = queue.popleft()
            newNode = newNodes[node]

            for neigh in node.neighbors:
                if neigh not in newNodes:
                    newNodes[neigh] = Node(neigh.val, [])
                    queue.append(neigh)
                
                newNodes[node].neighbors.append(newNodes[neigh])