class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        range_lst = {}
        min_val, max_val, min_cand = 0,0, 0
        for i in range(len(nums)):
            for key, value in range_lst.items():
                if nums[i] > key and nums[i] < value:
                    return True
             
            
            if i == 0:
                min_val, max_val, min_cand = nums[i], nums[i], nums[i]
            
            if nums[i] < min_cand:
                min_cand = nums[i]
            if nums[i] > min_cand: 
                max_val = nums[i]
                min_val = min_cand
                
                if min_val in range_lst:
                    if range_lst[min_val] < max_val:
                        range_lst[min_val] = max_val
                else:
                    range_lst[min_val] = max_val
                
        return False