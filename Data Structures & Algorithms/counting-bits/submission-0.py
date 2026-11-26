class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        dp[0] = 0
        exp = 1
        curr = 1
        while curr <= n:
            if curr == exp*2:
                exp *= 2
            # if curr >= 3:
            #     print(dp)
            #     print(curr)
            #     print(exp)
            dp[curr] = 1 + dp[curr - exp]
            curr += 1
        return dp