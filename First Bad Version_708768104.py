# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n
        while lo <= hi:
            mid = (lo + hi)//2
            if isBadVersion(mid) is True:
                hi = mid - 1
            else:
                lo = mid + 1
            print(lo, hi)
        return lo
