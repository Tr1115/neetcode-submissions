class Solution:
    def reverseBits(self, n: int) -> int:
        res = n
        res = (res >> 16) + (res << 16)
        res = (res >> 8 & 0x00ff00ff) + (res << 8 & 0xff00ff00)
        res = (res >> 4 & 0x0f0f0f0f) + (res << 4 & 0xf0f0f0f0)
        res = (res >> 2 & 0x33333333) + (res << 2 & 0xcccccccc)
        res = (res >> 1 & 0x55555555) + (res << 1 & 0xaaaaaaaa)
        return res 