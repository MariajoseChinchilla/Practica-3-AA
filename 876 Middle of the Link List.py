class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len_list = 0
        start = node = head
        while start:
            len_list = len_list + 1
            start = start.next
        middle = int(len_list/2)
        counter = 0
        while node:
            if counter == middle:
                return node
            else:
                counter = counter + 1
                node = node.next
        return None