class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # By assumption, there exists at least one peak
        lower, upper = 0, len(nums)-1
        while(lower < upper):
            mid = (upper+lower)//2
            if(nums[mid]<nums[mid+1]):
                lower = mid+1
            else:
                upper = mid
                
        return lower