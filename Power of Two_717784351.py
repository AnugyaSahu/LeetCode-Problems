class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        lo = 0
        hi = 30
        while lo <= hi:
            mid = (lo + hi)//2
            if 2**mid == n:
                return True
            elif 2**mid > n:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
