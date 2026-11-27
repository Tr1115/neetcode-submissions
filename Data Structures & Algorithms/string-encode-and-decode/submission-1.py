class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + ":" + s
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0 
        l = 0
        while i < len(s):
            if s[i] == ":":
                ans.append(s[i+1:i+1+l])
                i = i+1+l
                l = 0
            else:
                l *= 10
                l += (ord(s[i]) - ord('0'))
                i += 1

        return ans
