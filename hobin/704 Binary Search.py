class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bottom = 0
        top = len(nums)-1
        cur = len(nums) // 2
        
        def binary(cur, bottom, top):
            data = nums[cur]
                        
            if data == target:
                return cur
            elif nums[top] == target:
                return top
            elif nums[bottom] == target:
                return bottom
            elif top-cur == 1 and cur-bottom == 1:
                return -1
            elif len(nums) < 3:
                return -1
            elif data < target:
                bottom, cur = cur, (top-cur) // 2 + cur
            elif data > target:
                top, cur = cur, (cur - bottom) // 2 + bottom
            
            return binary(cur, bottom, top)
        
        return binary(cur, bottom, top)