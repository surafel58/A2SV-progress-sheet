class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.count = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str, value) -> None:

        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr.count += value
            curr = curr.children[char]
        
        curr.count += value
        curr.isEnd = True

    def search(self, word: str) -> bool:
        
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False

            curr = curr.children[char]
        
        return curr.isEnd

    def startsWith(self, prefix: str) -> int:
        
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0

            curr = curr.children[char]
        
        return curr.count
        
class MapSum:

    def __init__(self):
        self.trie = Trie()
        self.wordMap = dict()

    def insert(self, key: str, val: int) -> None:
        if key in self.wordMap:
            if self.wordMap[key] != val:
                self.trie.insert(key, val - self.wordMap[key])
        else:
            self.trie.insert(key, val)
        
        self.wordMap[key] = val
        

    def sum(self, prefix: str) -> int:
        return self.trie.startsWith(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
