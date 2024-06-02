class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]
        my = Counter(n)
        return my['1']
