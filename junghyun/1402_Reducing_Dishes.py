class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        #Hardy-Littlewood maximal inequality
        satisfaction.sort(reverse = True)
        length = len(satisfaction)
        summ, maxi = 0, 0
        sumlist = [0]*(length+1)
        for i in range(1, length+1):
            summ +=satisfaction[i-1]
            sumlist[i] = sumlist[i-1]+summ
            if maxi < sumlist[i]:
                maxi = sumlist[i]
        return maxi