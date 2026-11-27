class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        freq = [0] * 26
        for c in s1:
            freq[ord(c) - ord('a')] += 1

        for i in range(0, len(s1)):
            freq[ord(s2[i]) - ord('a')] -= 1

        l = 0
        r = len(s1) - 1
        while r+1 < len(s2):
            if all(x == 0 for x in freq):
                return True
            freq[ord(s2[l]) - ord('a')] += 1
            l += 1
            freq[ord(s2[r+1]) - ord('a')] -= 1
            r += 1 
        
        return all(x == 0 for x in freq)