
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      #Dictionary for easy retrieval using keys and O(1) time complexity for lookups, insertions, deletions
      my_dictionary = dict()
      for i in range(len(nums)):
        #if target is in the dictionary return the value using it as a key and its pair.
        if nums[i] in my_dictionary:
          return [my_dictionary[nums[i]], i]
        #if not, subtract it from target and store the difference in the dictionary with it being the key
        else:
          my_dictionary[target - nums[i]] = i

