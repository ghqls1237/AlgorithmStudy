class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if target <= nums[0]:
            return 0
        elif target > nums[length-1]:
            return length
        elif target == nums[length-1]:
            return length-1
        
        start, end = 0, length-1
        while (end - start) > 1:
            if(target == nums[(start+end)//2]):
                return (start+end)//2
            elif(target > nums[(start+end)//2]):
                start = (start+end)//2
            else:
                end = (start+end)//2
        if(start-end == 1):
            return end
        else:
            return start+1