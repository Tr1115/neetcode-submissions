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

        hm = defaultdict(list)
        for s in strs:
            hm[getFreqStr(s)].append(s)
        
        return list(hm.values())
        