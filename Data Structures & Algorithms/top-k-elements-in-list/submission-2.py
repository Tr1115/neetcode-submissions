class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        buckets = defaultdict(list)
        for num, count in freq.items():
            buckets[count].append(num)

        ans = []
        for j in range(len(nums), 0, -1):
            for num in buckets[j]:
                ans.append(num)
                if len(ans) == k:
                    return ans
