class Solution:
    def rob(self, nums: List[int]) -> int:
        # robmoney[i] = max robbed money until i th house
        robmoney = []
        length = len(nums)
        if length is 1:
            return nums[0]
        elif length is 2:
            return max(nums[0], nums[1])
        else:
            robmoney.append(nums[0])
            robmoney.append(max(nums[1], nums[0]))
        for i in range(2, length):
            if robmoney[i-2]+nums[i] > robmoney[i-1]:
                robmoney.append(robmoney[i-2]+nums[i])
            else:
                robmoney.append(robmoney[i-1])
                
        return robmoney[length-1]