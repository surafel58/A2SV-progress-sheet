# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = l1
        p2 = l2
        result = None
        temp = None

        sum = 0
        carry = 0

        while p1 and p2:
            sum = p1.val + p2.val + carry
            
            if result == None:
                result = ListNode(0, None)
                temp = result
            else:
                temp.next = ListNode(0, None)
                temp = temp.next
                
            if sum > 9:
                carry = sum // 10
                temp.val = sum % 10
            else:
                temp.val = sum 
                carry = 0

            p1 = p1.next
            p2 = p2.next

        while p1:
            sum = p1.val + carry

            if result == None:
                result = ListNode(0, None)
                temp = result
            else:
                temp.next = ListNode(0, None)
                temp = temp.next
                
            if sum > 9:
                carry = sum // 10
                temp.val = sum % 10
            else:
                temp.val = sum 
                carry = 0

            p1 = p1.next

        while p2:
            sum = p2.val + carry

            if result == None:
                result = ListNode(0, None)
                temp = result
            else:
                temp.next = ListNode(0, None)
                temp = temp.next
                
            if sum > 9:
                carry = sum // 10
                temp.val = sum % 10
            else:
                temp.val = sum 
                carry = 0
                
            p2 = p2.next

        if carry != 0:
            temp.next = ListNode(carry, None)
            temp = temp.next
            
        return result
