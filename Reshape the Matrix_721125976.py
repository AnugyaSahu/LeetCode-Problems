class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        
        total = []
        for i in mat:
            for j in i:
                total.append(j)
                
        new_mat = [[0] * c for i in range(r)]
        for i in range(r):
            for j in range(c):
                new_mat[i][j] = total[j + (i * c)]
                
        return new_mat
