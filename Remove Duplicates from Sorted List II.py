# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        dummy = ListNode()
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                next = curr.next
                while next and next.val == curr.val:
                    next = next.next

                prev.next = next
                curr = prev.next

            else:
                curr = curr.next
                prev = prev.next

        return dummy.next


            
        
