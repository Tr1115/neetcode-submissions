class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        A1: Hashing
            - Note freq of all elements in OrderedDict
            - Give the Kth top
            - O(n) Space
            - O(nlogn) Time [to maintain dict order]
            
        Optimizations:
            - Again bucket the elems based on frequency
            - 1 to n buckets
            - O(n) Space [2n space]
            - O(n) Time [2n time]

        Edge cases:
            - Empty array? No problem
            - -ve nums? Alright
            - k == 0?? => Empty array return

        Advanced:
            - Dynamic count of buckets 
                - if freq is n-1 of something
                - Only 1 other num is left with freq 1!
                - No need to form other buckets
            - Optimised counting [assert Summ(freq) == n]
                - If n-x has some element,
                - directly go to xth index
                - Because the 2nd highest freq needs to be x at max
        """
        # Storing freq of all nums and max_freq value
        freq = defaultdict(int)
        max_freq = 0
        for num in nums:
            freq[num] += 1
            max_freq = max(freq[num], max_freq)

        # creating max_freq+1 buckets
        arr = [[] for _ in range(max_freq + 1)]

        # Adding keys to bucets based on freq val
        for key, v in freq.items():
            arr[v].append(key)
        
        # Advanced optimisized counting
        elems_avail = len(nums)
        idx = max_freq
        res = []
        while k > 0 and idx > 0:
            # Bucket non empty, add elems in bucket
            # Update idx to next possible max freq
            elem_count = len(arr[idx])
            if elem_count > 0:
                res += arr[idx]
                k -= elem_count
                n = idx * elem_count
                idx = min(elems_avail - idx, idx-1)
                elems_avail -= n
            else: # bucket was empty, look at prev bucket
                idx -= 1
        return res




