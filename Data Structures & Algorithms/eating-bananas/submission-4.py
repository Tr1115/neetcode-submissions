
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1 
        high = max(piles)
        while low < high:
            mid = (low + high) // 2
            val = sum(math.ceil(p / mid) for p in piles)
            if val > h:
                low = mid + 1
            else:
                high = mid - 1

        while low >= 1 and sum(math.ceil(p / low) for p in piles) <= h:
            low -= 1
        return low+1
    