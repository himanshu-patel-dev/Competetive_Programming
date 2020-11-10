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
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
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
        curr, prev = slow.next, None
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
            remain_head1 = head1.next
            head1.next = head2
            head1, head2 = head2, remain_head1 
        
        return head         

def printLL(head):
    while head.next:
        print(head.val,end='->')
        head = head.next
    print(head.val)

if __name__ == "__main__":
    ll1 = ListNode(1)
    ll2 = ListNode(2)
    ll3 = ListNode(3)
    ll4 = ListNode(4)
    ll1.next = ll2
    ll2.next = ll3
    ll3.next = ll4
    s = Solution()

    printLL(ll1)
    printLL( s.reorderList(ll1) )
