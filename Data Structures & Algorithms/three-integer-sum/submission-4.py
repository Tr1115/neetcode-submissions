class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        i = 0
        print(nums)
        while i+2 < n:
            prev = nums[i]
            l = i+1 
            r = n-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    prevLeft = nums[l]
                    while l < n and nums[l] == prevLeft:
                        l += 1
                elif total < 0:
                    prevLeft = nums[l]
                    while l < n and nums[l] == prevLeft:
                        l += 1
                elif total > 0:
                    prevRight = nums[r]
                    while r >= 0 and nums[r] == prevRight:
                        r -= 1
            while i < n and nums[i] == prev:
                i += 1
        return ans