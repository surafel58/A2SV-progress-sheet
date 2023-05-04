class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        word_freq = Counter(words)
        words = []
        for word in word_freq:
            words.append([-word_freq[word], word])

        heapq.heapify(words)
        topk = []

        for i in range(k):
            value = heapq.heappop(words)
            value[0] *= -1
            topk.append(value)

        # print(topk)

        for i in range(len(topk)):
            topk[i] = topk[i][1]
        
        # print(topk)

        return topk
