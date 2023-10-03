class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:

        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
            curr.count += 1
        
        curr.isEnd = True

    def search(self, word: str) -> bool:
        
        curr = self.root
        result = curr.count

        for char in word:
            curr = curr.children[char]
            result += curr.count
        
        return result

        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = Trie()
        result = []

        for word in words:
            trie.insert(word)
        
        for word in words:
            result.append(trie.search(word))

        return result
