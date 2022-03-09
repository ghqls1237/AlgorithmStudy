class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 2022-03-03

        # First Trial 

        # Time Complexity: O(log n) /   Runtime: faster than 95.13%
        # Space Complexity: O(n) /   Memory Usage: less than 9.27% 
        # 함수가 재귀적으로 스택에 쌓이게 되므로
        
        def bin(_left, _right):
            # if _left >= len(nums) or _right < 0:
            #     return -1
            if _left > _right:
                return -1
            mid = (_right + _left) // 2
            # print(_left, _right, cur_n)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bin(mid + 1, _right)
            else:
                return bin(_left, mid - 1)


        return bin(0, len(nums) - 1)


        # ===========================================================
        # Second Trial 
        
        # Time Complexity: O(log n) /   Runtime: faster than 67.98%
        # Space Complexity: O(1) /   Memory Usage: less than 55.19% 

        left, right = 0, len(nums - 1)

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1



