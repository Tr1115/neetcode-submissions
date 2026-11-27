class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        last = {}
        for r in range(len(s)):
            if s[r] in last:
                l = max(l, last[s[r]] + 1)
            last[s[r]] = r
            ans = max(ans, r-l+1)
        return ans