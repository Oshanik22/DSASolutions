# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree = self.ser(root)
        tree = tree[:-1]
        return tree
        
    def ser(self, root):
        if not root:
            return "n,"
        tree = str(root.val) + ","
        tree += self.ser(root.left)
        tree += self.ser(root.right)
        return tree

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # # Reverse the elements so its more efficient to pop them off
        elements = data.split(",")
        elements = elements[::-1]
        print(elements)
        return self.makeTree(elements)
    
    def makeTree(self, elements):
        val = elements.pop()
        if val == "n":
            return None
        node = TreeNode(int(val))
        node.left = self.makeTree(elements)
        node.right = self.makeTree(elements)

        return node


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))