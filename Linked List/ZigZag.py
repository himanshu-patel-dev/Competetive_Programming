"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.
Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head:
            return head
        
        fast = slow = head
        # find the mid of LL
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        
        # reverse the second half of LL and terminate both so that there no cycle
        curr, prev, nextp = slow.next, None, None
        while curr:
            curr.next, curr, prev = prev, curr.next, curr
        slow.next = None # to remove cycle
        
        
        # now we have first half of LL in head1
        # and reversed second half in head2 
        # both LL do not have cycle
        head1, head2 = head, prev
        while head2:    # because second LL is shorted in case of odd element 
            # write both LL start to end and observer
            # final LL make a zig zag move in between both
            nxt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nxt
        
        return head
        
        
            
            
            
            