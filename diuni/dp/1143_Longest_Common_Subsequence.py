class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        
        # 2022-03-09
        # Bottom-up

        # Time Complexity: O(mn) /   Runtime: faster than 81.00%
        # Space Complexity: O(mn) /   Memory Usage: less than 67.74% 
        
        n, m = len(text1), len(text2)
        
        dp = [[0] * (m + 1) for i in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[n][m]
            