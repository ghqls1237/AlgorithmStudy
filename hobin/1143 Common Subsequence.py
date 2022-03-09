class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lcs = list()
        for i in range(1+len(text1)):
            tmp = []
            for j in range(1+len(text2)):
                tmp.append(0)
            lcs.append(tmp)

        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                if i == 0 or j == 0:
                    lcs[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                else:
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

        return lcs[-1][-1]