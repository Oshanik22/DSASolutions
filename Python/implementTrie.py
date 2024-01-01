class Trie:

    def __init__(self):
        self.trie = TrieNode('.')        

    def insert(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.eow = True

    def search(self, word: str) -> bool:
        node = self.trie
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.eow

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.eow = False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)