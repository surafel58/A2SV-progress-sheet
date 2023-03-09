# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head

        middle = self.middleNode(head)

        left = self.sortList(head)
        right = self.sortList(middle)

        return self.mergeTwoLists(left, right)

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        fast = dummy
        slow = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None
        
        return temp

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
