# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reverser_head=self.reverseList(head)
        cur=reverser_head
        pos=1
        while cur!=None:
            if n==1:
                cur=cur.next
                reverser_head=cur
                break
            if pos==n-1:
                cur.next=cur.next.next
                break
            else:
                cur=cur.next
            pos+=1
        final_head=self.reverseList(reverser_head)
        return final_head

    def reverseList(self, head):
        prev=None
        next=None
        cur=head
        while cur!=None:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        return prev






                