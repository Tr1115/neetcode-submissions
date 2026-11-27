class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getFreqStr(s: str) -> str:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            ans = ""
            for i in range(26):
                if freq[i] > 0:
                    ans += str(freq[i]) + str(i) + ", "
            return ans

        hm = dict()
        for s in strs:
            key = getFreqStr(s)
            if key not in hm:
                hm[key] = []
            hm[key].append(s)
        
        ans = []
        for val in hm.values():
            ans.append(val)
        
        return ans
        