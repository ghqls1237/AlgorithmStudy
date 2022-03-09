class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        result = []
        sum = 0
        if satisfaction[0] < 0:
            return 0
        
        for i in range(len(satisfaction)):
            for j in range(i+1):
                sum = sum + satisfaction[j]
            result.append(sum)
        return max(result)