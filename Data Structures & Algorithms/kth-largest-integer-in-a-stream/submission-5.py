import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for n in nums:
            if len(self.pq) < k:
                heapq.heappush(self.pq, n)
            else:
                if n >= self.pq[0]:
                    heapq.heappop(self.pq)
                    heapq.heappush(self.pq, n)

    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, val)
        elif len(self.pq) == self.k and val >= self.pq[0]:
            heapq.heappop(self.pq)
            heapq.heappush(self.pq, val)
        return self.pq[0]
