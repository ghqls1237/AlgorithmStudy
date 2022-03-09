class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Top-down

        # Time Complexity: O(n) /   Runtime: faster than 84.15%
        # Space Complexity: O(n) /   Memory Usage: less than 5.6% 
        
        def robORnot(i, _nums, memo):
            if i == 0:
                return _nums[0]
            elif i == 1:
                return max(_nums[0:2])
            else:            
                if i not in memo:
                    memo[i] = max(robORnot(i - 1, _nums, memo), robORnot(i - 2, _nums, memo) + _nums[i])
                return memo[i]
        
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0:2])
        else:
            memo1 = {}
            memo2 = {}
            return max(robORnot(n - 2, nums[:n-1], memo1), robORnot(n - 2, nums[1:], memo2))


        # Bottom-up

        # Time Complexity: O(n) /   Runtime: faster than 56.45%
        # Space Complexity: O(n) /   Memory Usage: less than 69.74% 

        def tab(_nums):
            n = len(_nums)
            money = [0] * n
            money[0] = _nums[0]
            money[1] = max(_nums[:2])

            for i in range(2, n):
                money[i] = max(money[i - 2] + _nums[i], money[i - 1])
            return money[n - 1]
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[:2])
        
        return max(tab(nums[:n-1]), tab(nums[1:]))
