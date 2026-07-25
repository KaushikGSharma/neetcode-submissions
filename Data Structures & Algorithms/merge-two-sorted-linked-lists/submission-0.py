# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        cur=dummy
        cur1=list1
        cur2=list2

        while cur1!=None and cur2!=None:
            if cur1.val<cur2.val:
                cur.next=cur1
                cur=cur.next
                cur1=cur1.next
            else:
                cur.next=cur2
                cur=cur.next
                cur2=cur2.next
        while cur1:
            cur.next=cur1
            cur=cur.next
            cur1=cur1.next
        while cur2:
            cur.next=cur2
            cur=cur.next
            cur2=cur2.next
        return dummy.next
        
            
