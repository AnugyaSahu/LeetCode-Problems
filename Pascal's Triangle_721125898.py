class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        if numRows == 1:
            return pascal
        pascal.append([1,1])
        if numRows == 2:
            return pascal
        for i in range(2, numRows):
            pascal.append([0]*(i+1))
            pascal[i][0], pascal[i][-1] = 1, 1
            for j in range(1, len(pascal[i][1:-1])+1):
                pascal[i][j] = pascal[i-1][j-1]+ pascal[i-1][j]
        return pascal
