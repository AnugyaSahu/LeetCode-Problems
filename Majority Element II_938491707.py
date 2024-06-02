class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        for i in nums:
            if i in nums_dict.keys():
                continue
            else:
                nums_dict[i] = nums.count(i)
        n = len(nums)
        result = []
        for key, value in nums_dict.items():
            if value > n//3:
                result.append(key)
        
        return result

