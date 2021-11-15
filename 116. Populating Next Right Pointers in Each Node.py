class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = collections.deque()
        q.append(root)

        while q:
            curr = q.popleft()
            if curr.left:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                q.append(curr.left)
                q.append(curr.right)
        return root