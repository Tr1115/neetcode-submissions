class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l = 0
        maxCount = 0
        ans = 0
        for r in range(len(s)):
            key = ord(s[r]) - ord('A')
            freq[key] += 1
            maxCount = max(maxCount, freq[key])
            while r-l+1 - maxCount > k:
                freq[ord(s[l]) - ord('A')] -= 1 
                maxCount = max(freq)
                l += 1 
            ans = max(ans, r-l+1)
        
        return ans