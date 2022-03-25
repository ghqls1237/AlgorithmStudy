# 2022-03-24

# First Trial 

# Time Complexity: O(n) /   Runtime: faster than 28.58%
# Space Complexity: O(1) /   Memory Usage: less than 80.46%

class Solution(object):
    def decodeString(self, s):
        stack = []
        
        for i in s:
            repeat = ""
            num = ""
            if i == "]":
                while True:
                    pop = stack.pop()
                    if pop == "[":
                        break
                    repeat = pop + repeat
                while stack:
                    pop = stack.pop()
                    if pop.isdigit():
                        num = pop + num
                    else:
                        stack.append(pop)
                        break
                num = int(num)
                stack.append(num * repeat)
            else:
                stack.append(i)
        
        ans = ""
        while True:
            if len(stack) == 0:
                break
            pop = stack.pop()
            ans = pop + ans
            
        return ans
                
        
# =========================================================
# Other's Solution

# Time Complexity: O(n) /   Runtime: faster than 6.91%
# Space Complexity: O(1) /   Memory Usage: less than 54.18%

class Solution(object):
    def decodeString(self, s):
        stack = []
        curString = ""
        curNum = 0
        for c in s:
            if c == "[":
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = 0
            elif c == "]":
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curString += c
        
        return curString