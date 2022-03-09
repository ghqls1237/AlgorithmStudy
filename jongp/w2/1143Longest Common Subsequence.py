class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1="t"+text1
        text2="t"+text2
        
        m=len(text1)
        n=len(text2)
        dp=[[0]*(m) for _ in range(n)]
        
        ans=0
        for i in range(1,n):
            for j in range(1,m):
                if text1[j]==text2[i]:
                    dp[i][j]=1+dp[i-1][j-1]
                    if dp[i][j]>ans:
                        ans=dp[i][j]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                    
        
        return ans