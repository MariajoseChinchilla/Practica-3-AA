class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0, next=head)
        s = d
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                s.next = head.next
            else:
                s = s.next
            head = head.next
        return d.next