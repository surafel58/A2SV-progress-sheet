class Solution:
    def maxProduct(self, words: List[str]) -> int:

        bin_words = []
        maxProduct = 0

        #record the letter occurence as binary number
        for i in range(len(words)):
            
            bin_word = 0

            for char in words[i]:
                bin_word |= 1 << (ord(char) - 97)
            
            bin_words.append(bin_word)

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not (bin_words[i] & bin_words[j]): 
                    maxProduct = max(maxProduct, (len(words[i]) * len(words[j])))
        
        return maxProduct
