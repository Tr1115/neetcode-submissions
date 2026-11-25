import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for s in stones:
            heapq.heappush(pq, -s)

        while len(pq) >= 2:
            a, b = heapq.heappop(pq), heapq.heappop(pq)
            if a == b:
                continue
            else:
                heapq.heappush(pq, a-b)
        
        return -pq[0] if len(pq) else 0