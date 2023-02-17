# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        ptr1 = head1
        ptr2 = head2

        result = None
        current = None

        while ptr1 != None and ptr2 != None:
            
            if ptr1.val < ptr2.val:
                if result == None:
                    result = ListNode(ptr1.val, None)
                    current = result
                else:
                    current.next = ListNode(ptr1.val, None)
                    current = current.next
                ptr1 = ptr1.next
            
            else:
                if result == None:
                    result = ListNode(ptr2.val, None)
                    current = result
                else:
                    current.next = ListNode(ptr2.val, None)
                    current = current.next
                ptr2 = ptr2.next

        while ptr1 != None:
            if result == None:
                result = ListNode(ptr1.val, None)
                current = result
            else:
                current.next = ListNode(ptr1.val, None)
                current = current.next
            
   
            ptr1 = ptr1.next

        while ptr2 != None:
            if result == None:
                result = ListNode(ptr2.val, None)
                current = result
            else:
                current.next = ListNode(ptr2.val, None)
                current = current.next
            

            ptr2 = ptr2.next

        return result
                    
