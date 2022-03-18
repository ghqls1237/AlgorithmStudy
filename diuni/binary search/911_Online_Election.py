import bisect


class TopVotedCandidate(object):

    # 2022-03-16

    # First Trial 

    # Time Complexity: O(log n) /   Runtime: faster than 51.35%
    # Space Complexity: O(n) /   Memory Usage: less than 54.05% 

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.result = []
        self.times = times
        can_dict = {}
        max_can, max_val = -1, 0
        
        for p in persons:
            if p not in can_dict:
                can_dict[p] = 0
            can_dict[p] += 1
            if max_val == max(can_dict.values()):
                if can_dict[p] == max_val:
                    max_can = p
            if max_val < max(can_dict.values()):
                max_can = p
                max_val = max(can_dict.values())
            self.result.append(max_can)
        

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        # print(self.result)
        left, right = 0, len(self.times) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.times[mid] == t:
                return self.result[mid]
            elif self.times[mid] < t:
                left = mid + 1
            else:
                right = mid - 1
        
        if self.times[mid] > t:
            mid -= 1
        return self.result[mid]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)



    # =======================================================
    # Other's Solution

    # Time Complexity: O(log n) /   Runtime: faster than 89.19%
    # Space Complexity: O(n) /   Memory Usage: less than 64.86% 

    def __init__(self, persons, times):
        self.leads, self.times, count = [], times, {}
        lead = -1
        for p in persons:
            count[p] = count.get(p, 0) + 1 
            # get(p, 0): count의 p라는 key의 value를 가져오되 없으면 default 값을 0으로
            if count[p] >= count.get(lead, 0):  lead = p
            self.leads.append(lead)

    def q(self, t):
        return self.leads[bisect.bisect(self.times, t) - 1]
        # return self.leads[bisect.bisect_right(self.times, t) - 1]
        # 둘 다 됨

        '''
        bisect_left, right 차이

        1. 해당 값이 리스트에 있을 때
          bisect_left - 해당 index 반환
          bisect_right - 해당 index+1 반환

            lst= [1, 4, 6, 10]

            print(bisect_left(lst, 6)) # result = 2
            print(bisect_right(lst , 6)) # result = 3

        2. 해당 값이 리스트에 없을 때
          bisect_left - 리스트 오름차순에 들어갈 index 반환
          bisect_right - 리스트 오름차순에 들어갈 index 반환

            print(bisect_left(lst, 9)) # result = 3
            print(bisect_right(lst , 9)) # result = 3
            
        '''
