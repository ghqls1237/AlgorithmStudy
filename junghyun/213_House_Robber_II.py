class Solution:
    def rob(self, nums: list[int]) -> int:
        # 1 is rob 1st house, vise versa for 2
        # if 1, then rob among 2,3,...,n-2 th element
        # if 2, then rob among 1,2,..,n-1 th element
        
        length = len(nums)
        if length is 1:
            return nums[0]
        elif length is 2:
            return max(nums[0], nums[1])
        elif length is 3:
            return max(nums[0], max(nums[1], nums[2]))
        
        maxrob1 = [0,0]
        maxrob2 = [0,nums[1]]
        
        for i in range(2, length-1):
            if maxrob1[i-2] + nums[i] > maxrob1[i-1]:
                maxrob1.append(maxrob1[i-2] + nums[i])
            else:
                maxrob1.append(maxrob1[i-1])
            if maxrob2[i-2] + nums[i] > maxrob2[i-1]:
                maxrob2.append(maxrob2[i-2] + nums[i])
            else:
                maxrob2.append(maxrob2[i-1])
                
        if maxrob2[length-3]+nums[length-1] > maxrob2[length-2]:
            maxrob2.append(maxrob2[length-3]+nums[length-1])
        else:
            maxrob2.append(maxrob2[length-2])
            
        if maxrob2[length-1] > maxrob1[length-2] + nums[0]:
            return maxrob2[length-1]
        else:
            return maxrob1[length-2]+nums[0]