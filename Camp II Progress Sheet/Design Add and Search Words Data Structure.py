#.ab
#a.b
#ab.
#..b
#.a.
#a..

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root 

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]

        curr.isEnd = True

    def search(self, word: str) -> bool:
        
        def dfs(index, node, word):
            
            if index == len(word):
                return node.isEnd

            char = word[index]
            if char == ".":
                for child in node.children:
                    if dfs(index + 1, node.children[child], word):
                        return True

            else:
                if char in node.children:
                    if dfs(index + 1, node.children[char], word):
                        return True
                    
                    return False

        return dfs(0, self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
