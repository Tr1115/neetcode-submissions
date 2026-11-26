class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            if n in s:
                return False
            s.add(n)
            digits = [int(d) for d in str(n)]
            n = sum([d*d for d in digits])
        return True