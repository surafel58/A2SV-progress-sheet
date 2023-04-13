# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if head.next == None or left == right:
            return head

        i = 1
        curr = head
        
        leftNode = None
        rightNode = None

        leftPrev = ListNode(0)
        rightNext = None
        
        while True:
            
            #hold the prev of left node
            if i == left - 1:
                leftPrev = curr

            #hold the left node
            if i == left:
                leftNode = curr

            #hold the right node
            if i == right:
                rightNode = curr

                #hold the next node of the right node
                rightNext = curr.next
                break

            curr = curr.next
            i += 1
        
        # print(leftPrev.val, rightNext.val)
        
        #reverse the node between left and right
        reversedHead = self.reverse(leftNode, rightNode)

        #rearrange the list 
        leftPrev.next = rightNode
        leftNode.next = rightNext
        
        #edge case
        if left == 1:
            head = leftPrev.next

        return head

    def reverse(self, left, right):
        # pointers that traverse through the linked list  
        current = left
        next = None
        prev = None

        rightVal = right.next

        #iterate through the list to reverse it
        while(current != rightVal):
            next = current.next
            current.next = prev
            prev = current
            current = next
    
        #assign head to the last element
        head = prev
        
        return head
