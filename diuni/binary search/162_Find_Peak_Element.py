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

        '''
        if an element(not the right-most one) is smaller than its right neighbor, 
         then there must be a peak element on its right, because the elements on its right is either 
           1. always increasing  -> the right-most element is the peak
           2. always decreasing  -> the left-most element is the peak
           3. first increasing then decreasing -> the pivot point is the peak
           4. first decreasing then increasing -> the left-most element is the peak  

           Therefore, we can find the peak only on its right elements( cut the array to half)
        '''
         
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
        

        # ===================================
        # Other's Solution
        # padding 주기

        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
           
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            
            if nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1


