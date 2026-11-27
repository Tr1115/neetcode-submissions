class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0 
        n = len(heights)
        l = 0 
        r = n - 1
        while l < r:
            # print(heights[l])
            # print(heights[r])
            # print(r-l)
            # print(ans)
            # print("[[[[]]]")
            ans = max(ans, min(heights[l], heights[r]) * (r-l))
            # left = min(heights[l+1], heights[r])
            # right = min(heights[l], heights[r-1])
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans
            