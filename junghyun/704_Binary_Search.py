class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums)-1
        if(nums[start] == target):
            return start
        elif(nums[end] == target):
            return end
        
        while(end-start > 1):
            idx = start + (end-start)//2
            if(target == nums[idx]):
                return idx
            elif(target > nums[idx]):
                start = idx
            else:
                end = idx  
        return -1

# sol = Solution()
# nums = [-1,0,3,5,9,12]
# target = 9

# ans = sol.search(nums, target)
# print(ans)