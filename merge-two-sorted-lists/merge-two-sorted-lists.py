# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = ListNode(0)# save head and tail pos initializing purpose
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1= l1.next
            else:
                tail.next = l2
                l2= l2.next
            tail= tail.next
        tail.next = l1 if l1 else l2
        return head.next #coz head will be 0 as initialized earlier
                
        
        