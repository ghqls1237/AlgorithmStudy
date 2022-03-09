class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        le,ri,res=0,len(nums)-1,0
        
        while le<=ri:
            mid=(le+ri)//2
            
            if nums[mid]<target:
                res=mid+1
                le=mid+1
            else:
                ri=mid-1
        return res
            