class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        lo = 0
        hi = n-1
        while lo <= hi:
            mid = (lo+hi)//2
            if target in matrix[mid]:
                low = 0
                high = m-1
                while low <= high:
                    mid_mid = (low+high)//2
                    if matrix[mid][mid_mid] == target:
                        return True
                    elif matrix[mid][mid_mid] < target:
                        low = mid_mid + 1
                    else:
                        high = mid_mid - 1
            elif target > matrix[mid][-1]:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
