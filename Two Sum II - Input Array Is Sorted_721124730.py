class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my = dict()
        for i, s in enumerate(numbers):
            if s in my:
                index1 = my[s]
                return [index1 + 1, i + 1]
            else:
                my[target - s] = i 
