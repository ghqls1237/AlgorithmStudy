class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 2022-03-07

        # First Trial 

        # Time Complexity: O(log n) /   Runtime: faster than 11.24%
        # Space Complexity: O(1) /   Memory Usage: less than 44.44% 

        # Lets say you have a mid number at index x, nums[x]
        # if (num[x+1] > nums[x]), 
        # that means a peak element HAS to exist on the right half of that array, 
        # because (since every number is unique) 
        # 1. the numbers keep increasing on the right side, and the peak will be the last element. 
        # 2. the numbers stop increasing and there is a 'dip', or there exists somewhere a number such that nums[y] < nums[y-1], which means number[x] is a peak element.


        n = len(nums)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_right = float("-inf") if mid == n - 1 else nums[mid + 1]
            mid_left = float("-inf") if mid == 0 else nums[mid - 1]
           
            if nums[mid] > mid_left and nums[mid] > mid_right:
                return mid
            
            if mid_right > mid_left:
                left = mid + 1
            else:
                right = mid - 1
        

