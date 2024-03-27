class WordDictionary:

    def __init__(self):
        self.trie = TrieNode('root')

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.eow = True

    def search(self, word: str) -> bool:
        def dfs(curr, i):
            if i == len(word):
                return curr.eow
            
            if word[i] == '.':
                for child in curr.children:
                    if dfs(curr.children[child], i+1):
                        return True
            
            if word[i] not in curr.children:
                return False
            
            return dfs(curr.children[word[i]], i+1)

        return dfs(self.trie,0)
        
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.eow = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)