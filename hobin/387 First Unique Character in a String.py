class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt_map = {}
        for i in range(len(s)):
            if s[i] in cnt_map:
                cnt_map[s[i]].append(i)
            else:
                cnt_map[s[i]] = [i]
        
        for k, v in cnt_map.items():
            if len(v) == 1:
                return v[0]
            
        return -1