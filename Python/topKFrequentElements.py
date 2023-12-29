class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1
        
        minHeap = []

        for num,freq in freq.items():
            if len(minHeap) == k:
                heapq.heappushpop(minHeap, (freq, num))
            else:
                heapq.heappush(minHeap, (freq, num))

        return [num for (freq, num) in minHeap]
