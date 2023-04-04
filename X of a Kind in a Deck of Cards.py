class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        def findGcf(a, b):
            if b == 0:
                return a

            return findGcf(b, a % b)
                
        
        freq = Counter(deck)

        gcf = freq[deck[0]]
        for key in freq:
            gcf = findGcf(gcf, freq[key])

        return gcf != 1 
