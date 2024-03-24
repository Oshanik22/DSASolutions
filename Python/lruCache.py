class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addNode(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node
    
    def deleteNode(self, node):
        prevv = node.prev
        nextt = node.next
        prevv.next = nextt
        nextt.prev = prevv

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        ans = node.val
        del self.map[key]
        self.deleteNode(node)
        self.addNode(node)
        self.map[key] = self.head.next

        return ans

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            currNode = self.map[key]
            del self.map[key]
            self.deleteNode(currNode)
        
        if len(self.map) >= self.capacity:
            del self.map[self.tail.prev.key]
            self.deleteNode(self.tail.prev)

        newNode = Node(key, value)
        self.addNode(newNode)
        self.map[key] = self.head.next
        
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)