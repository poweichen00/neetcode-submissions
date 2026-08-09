# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        pre = None
        while second:
            second.next, pre, second = pre, second, second.next
        first, second = head, pre
        while second:
            first1 = first.next
            second1 = second.next
            first.next = second
            second.next = first1
            first, second = first1, second1
