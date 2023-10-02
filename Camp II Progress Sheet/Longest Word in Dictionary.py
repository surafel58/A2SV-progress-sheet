class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.word = ""

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:

        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
        
        curr.isEnd = True
        curr.word = word

    def search(self, word: str) -> bool:
        prev = 0
        curr = self.root
        
        for char in word:
            if curr != self.root and (len(curr.word) - prev) != 1:
                return None
            
            prev = len(curr.word)
            curr = curr.children[char]

        return word

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False

            curr = curr.children[char]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = Trie()
        result = []
        for word in words:
            trie.insert(word)

        words.sort(reverse=True)

        for word in words:
            temp = trie.search(word)
            if temp:
                result.append(temp)

        freq = defaultdict(list)
        for word in result:
            freq[len(word)].append(word)
        
        if freq:
            result = freq[max(freq)]
            result.sort()

            return result[0]
        
        return ""
