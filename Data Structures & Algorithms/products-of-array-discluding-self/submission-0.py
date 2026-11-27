class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * (n + 1)
        right = [1] * (n + 1)
        for i in range(n):
            left[i+1] = left[i] * nums[i]

        for j in range(n-1, -1, -1):
            right[j] = right[j+1] * nums[j]

        ans = [0] * n
        for i in range(n):
            ans[i] = left[i] * right[i+1]

        return ans