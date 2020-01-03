# Sort List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail=head
        while tail.next:
            tail=tail.next
        self.quicksort(head,tail)
        return head        
        
    def quicksort(self,head,tail):
        if head!=tail:
            p,q=self.partition(head)
            self.quicksort(head,p)
            self.quicksort(q,tail)
        
    def partition(self,head):
        tail=head
        while tail.next:
            tail=tail.next
        key=tail.val
        small=ListNode(None)
        small.next=head
        cur=head
        while cur!=tail:
            if cur.val<=key:
                small=small.next
                self.exchange(small.val,cur.val)
            cur=cur.next
        self.exchange(small.next.val,tail.val)
        return small,small.next 
            
    def exchange(self,v1,v2):
        v1,v2=v2,v1
    