# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow=head
        fast=head

        # split into 2
        while slow and fast and fast.next:
            slow = slow.next
            fast= fast.next.next
        first=head
        second=slow.next
        slow.next=None

        #Reverse second
        prev=None
        cur=second
        next=None
        while cur!=None:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next

        # 
        first=head
        second = prev
        dummy=ListNode(0)
        temp = dummy
        i=0
        while first!=None and second !=None:
            if i%2==0:
                temp.next=first
                first=first.next
                temp=temp.next
            else:
                temp.next=second
                second=second.next
                temp=temp.next
            i+=1
        while first!=None:
            temp.next=first
            first=first.next
            temp=temp.next
        
        while second!=None:
            temp.next=second
            second=second.next
            temp=temp.next