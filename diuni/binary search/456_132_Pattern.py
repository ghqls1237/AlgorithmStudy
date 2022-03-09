# 2022.03.08
# First Trial

# Find Peak Element
# Wrong Answer
# counter example : [0, 2, 1, 3, 4, 5]

class Solution(object):
    def find132pattern(self, nums):
        

        n = len(nums)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            if mid == n - 1 or mid == 0:
                break
            if nums[mid] > nums[mid + 1] and nums[mid + 1] > nums[mid - 1]:
                return True
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

# Second Trial
# Time Limit Exceeded
    
from collections import deque

class Solution(object):
    def find132pattern(self, nums):
        
        
        left_stack = deque()
        right_stack = deque(nums)
        
        left_stack.append(right_stack.popleft())
        min_left = min(left_stack)
        
        
        for i in range(len(nums) - 1):
            peak = right_stack.popleft()
            if min_left < peak:
                for r in right_stack:
                    if min_left < r < peak:
                        return True
            else:
                min_left = peak
        return False
            

# Third Trial (다른 사람 풀이 참고)
# Time Limit Exceeded
          
            
class Solution(object):
    def find132pattern(self, nums):
        
        stack = []
        mins = []
        mins.append(nums[0])
        
        for i in range(1, len(nums)):
            mins.append(min(mins[i - 1], nums[i]))
        
        for i in range(len(nums) - 1, -1, -1):
            peak = nums[i]
            if stack:
                j = 0
                while True:
                    if j == len(stack):
                        break
                    if mins[i] >= stack[j]:
                        del stack[j]
                    else:
                        j += 1
                for j in range(len(stack)):
                    if mins[i] < stack[j] < peak:
                        return True
            stack.append(peak)
        return False
            
            
# Forth Trial (다른 사람 풀이 참고)
# Time Complexity: O(n) /   Runtime: faster than 61.97%
# Space Complexity: O(n) /   Memory Usage: less than 8.45% 
          
            
class Solution(object):
    def find132pattern(self, nums):
        
        stack = []
        mins = []
        mins.append(nums[0])
        
        for i in range(1, len(nums)):
            mins.append(min(mins[i - 1], nums[i]))
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > mins[i]:
                while stack and stack[-1] <= mins[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False    
        
        