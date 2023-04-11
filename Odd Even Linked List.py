# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #2,3,4,5,1
        # 1 2 3

        if not head or not head.next or not head.next.next:
            return head


        evenList = head.next 
        oddList = head

        even = evenList
        odd = oddList

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        
        odd.next = evenList

        return oddList
