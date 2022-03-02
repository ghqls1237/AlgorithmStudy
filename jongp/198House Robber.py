class Solution:
    def rob(self, nums: List[int]) -> int:
        prev=pprev=0
        
        for num in nums:
            cur=max(prev,pprev+num)
            pprev,prev=prev,cur
        

        return max(prev,cur)