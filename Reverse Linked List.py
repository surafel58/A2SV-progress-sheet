# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # pointers that traverse through the linked list  
        current = head
        next = None
        prev = None
        
        #iterate through the list to reverse it
        while(current != None):
            next = current.next
            current.next=prev
            prev = current
            current = next
    
        #assign head to the last element
        head = prev
                
        #return the pointer that points to the middle element
        return head
