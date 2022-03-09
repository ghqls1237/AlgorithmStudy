class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        top = len(nums)-1
        bottom = 0
        cur = len(nums) // 2
        def search(top, bottom, cur):
            if top == bottom:
                return top
            elif top == cur or bottom == cur:
                if nums[top] > nums[bottom]:
                    return top
                else:
                    return bottom
            elif nums[cur-1] < nums[cur] and nums[cur] > nums[cur+1]:
                return cur
            elif nums[cur] < nums[cur+1]:
                bottom, cur = cur, (top-cur) // 2 + cur
            elif nums[cur] < nums[cur-1]:
                top, cur = cur, (cur-bottom) // 2 + bottom 
            
            return search(top, bottom, cur)
        return search(top, bottom, cur)