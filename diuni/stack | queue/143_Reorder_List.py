# 2022-03-24

# First Trial 

# Time Complexity: O(n) /   Runtime: faster than 28.58%
# Space Complexity: O(1) /   Memory Usage: less than 80.46%

from collections import deque

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        first = deque([])
        second = deque([])
        curNode = head
        
        while curNode != None:
            nextNode = curNode.next
            curNode.next = None
            first.append(curNode)
            curNode = nextNode
        
        n = len(first)
        for _ in range(n // 2):
            second.append(first.pop())
        
        prevNode = None
        while first:
            curNode = first.popleft()
            if prevNode:
                prevNode.next = curNode
            if second:
                nextNode = second.popleft()
                curNode.next = nextNode
                prevNode = nextNode



# =========================================================
# Other's Solution

# Time Complexity: O(n) /   Runtime: faster than 89.31%
# Space Complexity: O(1) /   Memory Usage: less than 54.46%

# Find the middle
# 1) count number of elements and then divide
# 2) slow/fast iterators trick, where slow moves with speed 1 and fast moves with speed 2. 
#    Then when fast reches the end, slow will be in the middle, as we need.

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # step 1: find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # slow is now middle!

        # step 2: reverse second half
        prev, cur = None, slow.next
        while cur:
            nextt = cur.next
            cur.next = prev
            prev = cur
            cur = nextt
        slow.next = None
        
        # step 3: merge lists
        tail = prev
        while tail:
            nextt = head.next
            head.next = tail
            head = tail
            tail = nextt
        print(head)
        