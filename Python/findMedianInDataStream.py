class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= self.maxHeap[0][1]:
            heapq.heappush(self.maxHeap, (num * -1, num))
        else:
            heapq.heappush(self.minHeap, (num, num))
        self.balanceHeaps()

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0][1]+self.maxHeap[0][1])/2
        else:
            return self.maxHeap[0][1]
    
    def balanceHeaps(self):
        #if maxHeap is 2 more than minHeap, we need to balance
        if len(self.maxHeap) > len(self.minHeap) + 1:
            key, num = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, (num, num))
        elif len(self.minHeap) > len(self.maxHeap):
            key,num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, (num*-1, num))


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()