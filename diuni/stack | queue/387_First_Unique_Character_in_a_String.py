# 2022-03-24

# First Trial 

# Time Complexity: O(n) /   Runtime: faster than 42.03%
# Space Complexity: O(1) /   Memory Usage: less than 6.26%

from collections import deque, defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        ans = -1
        char_dict = defaultdict(int)
        queue = deque([])
        
        for c in s:
            queue.append(c)
            char_dict[c] += 1
        
        for i in range(len(s)):
            pop = queue.popleft()
            if char_dict[pop] == 1:
                return i
                    
        return ans


# =========================================================
# Other's Solution

# Time Complexity: O(n) /   Runtime: faster than 96.91%
# Space Complexity: O(1) /   Memory Usage: less than 95.50%

class Solution:
    def firstUniqChar(self, s):
        d = {}
        seen = set()
        
        for idx, c in enumerate(s):
            if c not in seen:
                d[c] = idx
                seen.add(c)
            elif c in d:
                del d[c]
        
        return min(d.values()) if d else -1