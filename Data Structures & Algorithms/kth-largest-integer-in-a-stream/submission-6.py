import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = [] # Space: O(k)

        for num in nums: # n iteration
            self._add_to_heap(num) # O(log k)
    
    def _add_to_heap(self, num):
        heapq.heappush(self.minHeap, num) # O(log k)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # O(log k)
        
    def add(self, val: int) -> int:
        self._add_to_heap(val) # O(log k)
        return self.minHeap[0]
