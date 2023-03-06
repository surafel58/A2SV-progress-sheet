# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeLists(list1, list2)

    def mergeLists(self, curr1, curr2):
        
        result = None
        if curr1 == None:
            return curr2
        elif curr2 == None:
            return curr1
        
        if curr1.val <= curr2.val:
            result = curr1
            result.next = self.mergeLists(curr1.next, curr2)

        else:
            result = curr2
            result.next = self.mergeLists(curr1, curr2.next)

        return result  

                    
