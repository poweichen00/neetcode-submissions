# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        grouppre = dummy
        while True:
            kth = self.getKth(grouppre, k)
            if not kth:
                break
            groupnext = kth.next
            pre, cur = kth.next, grouppre.next
            while cur != groupnext:
                cur.next, pre, cur = pre, cur, cur.next
            grouppre.next, grouppre = kth, grouppre.next
        return dummy.next
    def getKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur