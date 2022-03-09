class Solution(object):
    def maxSatisfaction(self, satisfaction):

        # 2022-03-09

        # Time Complexity: O(n ^ 2) /   Runtime: faster than 23.61%
        # Space Complexity: O(1) /   Memory Usage: less than 72.22% 
        
        satisfaction.sort()
        n = len(satisfaction)
        ans = 0
        
        for i in range(1, len(satisfaction) + 1):
            temp = 0
            for j in range(i, -1, -1):
                temp += j * satisfaction[n - 1 - (i - j)]
            ans = max(temp, ans)
        
        return ans