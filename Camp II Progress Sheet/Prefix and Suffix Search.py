class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.index = []

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, i, word: str) -> None:

        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr.index.append(i)
            curr = curr.children[char]
        
        curr.index.append(i)
        curr.isEnd = True

    def search(self, word: str) -> bool:
        
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False

            curr = curr.children[char]
        
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return [False, set()]

            curr = curr.children[char]
        
        return [True, curr.index]


class WordFilter:

    def __init__(self, words: List[str]):
        
        self.words = words
        self.trie = Trie()
        self.trie_reverse = Trie()
        
        for i, word in enumerate(words):
            self.trie.insert(i, word)
            self.trie_reverse.insert(i, word[::-1])        

    def f(self, pref: str, suff: str) -> int:

        result1 = self.trie.startsWith(pref)
        result2 = self.trie_reverse.startsWith(suff[::-1])
        
        if result1[0] and result2[0]:

            result1 = result1[1]
            result2 = result2[1]

            i = len(result1) - 1
            j = len(result2) - 1

            while i >= 0 and j >= 0:
                if result1[i] == result2[j]:
                    return result1[i]
                if result1[i] > result2[j]:
                    i -= 1
                else:
                    j -= 1

        return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
