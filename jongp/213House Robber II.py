class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0] #missed one
        
        prev1=pprev1=0 #visit 0th
        prev2=pprev2=0 #visit n-1th
        
        for i, num in enumerate(nums):
            
            if i!=len(nums)-1: #visit 0th
                cur=max(prev1,pprev1+num)
                prev1,pprev1=cur,prev1
                
            if i!=0: #visit n-1 th 
                cur=max(prev2,pprev2+num)
                prev2,pprev2=cur,prev2
                
                
                
        return max(prev1,prev2)