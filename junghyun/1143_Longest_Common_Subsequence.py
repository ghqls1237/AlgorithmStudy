class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1 = len(text1)
        length2 = len(text2)
        mat = [[0 for j in range(length1+1)] for i in range(length2+1)]
        for i in range(1, length1+1):
            for j in range(1, length2+1):
                if text1[i-1] == text2[j-1]:
                    mat[j][i] = (mat[j-1][i-1]+1)
                else:
                    mat[j][i] = max(mat[j-1][i], mat[j][i-1])
        return mat[length2][length1]


# sol = Solution()
# t1 = "abc"
# t2 = "abcabc"
# print(sol.longestCommonSubsequence(t1, t2))
