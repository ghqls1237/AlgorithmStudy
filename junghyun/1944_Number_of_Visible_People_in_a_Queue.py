# Runtime: 1344 ms, faster than 73.01%
# Memory Usage: 33.9 MB, less than 5.10% 

class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        cluster, stack, ans = [], [], []
        for i, h in reversed(list(enumerate(heights))):
            if cluster !=[]:
                if cluster[-1] < h:     #increasing, hence, compare stack
                    cluster.append(h)
                    cnt = 0
                    while stack != []:
                        if stack[-1] > h:
                            break
                        stack.pop()
                        cnt+=1
                    if len(stack) > 0:
                        cnt = cnt+1
                    stack.append(h)
                    ans.append(cnt)
                else:                   #decreasing, hence, update stack
                    cluster = []
                    ans.append(1)
                    cluster.append(h)
                    stack.append(h)
            else:
                cluster.append(h)
                stack.append(h)
                ans.append(0)
        return list(reversed(ans))
            

sol = Solution()
tar = [10,6,8,5,11,9]
ans = sol.canSeePersonsCount(tar)
print(ans)