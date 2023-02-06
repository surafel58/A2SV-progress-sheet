# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        resultHead = None
        current = head

        while current != None:
            if current.val < x:
                if resultHead == None:
                    resultHead = ListNode(current.val, None)
                else:
                    temp = resultHead
                    while temp.next != None:
                        temp = temp.next
                    newNode = ListNode(current.val, None)
                    temp.next = newNode
            current = current.next
        
        current = head
        while current != None:
            if current.val >= x:
                if resultHead == None:
                    resultHead = ListNode(current.val, None)
                else:
                    temp = resultHead
                    while temp.next != None:
                        temp = temp.next
                    newNode = ListNode(current.val, None)
                    temp.next = newNode
            current = current.next
    
        return resultHead
