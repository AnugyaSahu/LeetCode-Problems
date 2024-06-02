class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        n = [int(i) for i in n]
        return reduce(lambda x,y : x*y, n) - reduce(lambda x,y: x+y, n)
