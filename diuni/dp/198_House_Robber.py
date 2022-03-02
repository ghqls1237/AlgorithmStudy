class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 2022-03-02
        # Top-down

        # Time Complexity: O(n) /   Runtime: faster than 26.61%
        # Space Complexity: O(n) /   Memory Usage: less than 19.09% 

        memo = {}
        
        def robORnot(n):
            if n == 0:
                return nums[0]
            elif n == 1:
                return max(nums[:2])
            if n not in memo:
                memo[n] = max(robORnot(n - 2) + nums[n], robORnot(n - 1))
            return memo[n]
        
        return robORnot(len(nums) - 1)



        # Bottom-up

        # Time Complexity: O(n) /   Runtime: faster than 33.30%
        # Space Complexity: O(n) /   Memory Usage: less than 19.09% 

        n = len(nums)
    
        if n == 1:
            return nums[0]
        
        money = [0] * n
        money[0] = nums[0]
        money[1] = max(nums[:2])


        for i in range(2, n):
            money[i] = max(money[i - 2] + nums[i], money[i - 1])
        print(money)
        return money[n - 1]
            


    