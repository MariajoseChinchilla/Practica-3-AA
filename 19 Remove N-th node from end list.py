class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0, head)
        l = d
        r = head
        while n > 0 and r:
            r = r.next
            n = n - 1
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next

        return d.next