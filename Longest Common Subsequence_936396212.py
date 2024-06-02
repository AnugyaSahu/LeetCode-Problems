class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 , n2 = len(text1), len(text2)
        dyn = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        for i in range(n1):
            for j in range(n2):
                if text1[i] == text2[j]:
                    dyn[i+1][j+1] = 1+dyn[i][j]
                else:
                    dyn[i+1][j+1] = max(dyn[i][j+1], dyn[i+1][j])

        return dyn[-1][-1]
