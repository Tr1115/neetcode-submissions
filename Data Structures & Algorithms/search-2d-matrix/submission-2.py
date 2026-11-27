class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0 
        high = len(matrix)-1
        while low < high:
            mid = (low + high) // 2
            val = matrix[mid][0] 
            if target == val:
                return True
            if target < val:
                high = mid - 1
            else:
                low = mid + 1

        if matrix[low][0] > target:
            low -= 1

        lo = 0
        hi = len(matrix[low])-1
        while lo < hi:
            m = (lo + hi) // 2
            val = matrix[low][m]
            if target == val:
                return True
            if target < val:
                hi = m - 1
            else:
                lo = m + 1
        
        return matrix[low][lo] == target