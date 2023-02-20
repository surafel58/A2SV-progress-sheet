# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #1,1,1,1,1,2
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        fast = head.next
        slow = head

        while fast:
            
            while fast and slow.val == fast.val:
                slow.next = fast.next
                fast = fast.next
            
            if fast == None:
                return head

            slow = slow.next
            fast = fast.next

        return head
