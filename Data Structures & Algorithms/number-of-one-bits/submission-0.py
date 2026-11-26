class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 
        while n > 0:
            inc = 1 if n % 2 == 1 else 0 
            count += inc
            n = n // 2 
        return count