# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        lst = []
        cur = head
        while cur.next is not None:
            lst.append(cur.val)
            cur = cur.next
        lst.append(cur.val)
        
        cur = head
        
        front = 1
        back = len(lst)-1
        while front <= back:
            cur.next.val = lst[back]
            back = back -1 
            cur = cur.next
            if front <= back:
                cur.next.val = lst[front]
                front = front + 1
                cur = cur.next