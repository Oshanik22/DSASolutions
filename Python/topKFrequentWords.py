class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap, result = [], []
        for word in freq:
            heap.append((-freq[word], word))

        heapq.heapify(heap) #O(n)

        for i in range(k):
            freq, word = heapq.heappop(heap)
            result.append(word)

        return result