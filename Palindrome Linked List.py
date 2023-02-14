# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        reverseHead = None

        current = head

        while current != None:
            if reverseHead == None:
                reverseHead = ListNode(current.val, None)
            else:
                newNode = ListNode(current.val, reverseHead)
                reverseHead = newNode
            current = current.next

        current1 = head
        current2 = reverseHead

        while current1 != None:
            if current1.val != current2.val:
                return False
            current1 = current1.next
            current2 = current2.next
        
        return True
