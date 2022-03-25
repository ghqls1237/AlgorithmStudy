from curses.ascii import SO


class Solution:
    def decodeString(self, s: str) -> str:
        stack, multiNum, curString = [], 0, ''
        for char in s:
            if char == '[':
                stack.append(curString)
                stack.append(multiNum)    
                multiNum = 0
                curString = ''
            elif char == ']':
                n = stack.pop()
                curString = stack.pop() + n * curString
            elif char.isdigit():
                multiNum = 10*multiNum + int(char)
            else:
                curString+=char
        return curString


sol = Solution()
ans = sol.decodeString("3[a]2[bc]")
print(ans)