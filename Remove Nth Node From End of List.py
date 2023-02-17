# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        current = head 
        size = 0
        while current != None:
            size += 1
            current = current.next

        n = size - n

        if n == 0:
            head = head.next
            return head

        current = head

        i = 0
        while i < n - 1:
            current = current.next
            i += 1

        current.next = current.next.next

        return head
