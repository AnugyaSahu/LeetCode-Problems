class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            if target > nums[-1]:
                return len(nums)
            if target < nums[0]:
                return 0
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target > nums[mid-1]:
                return mid
            elif nums[mid] < target < nums[mid+1]:
                return mid+1
            elif nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
