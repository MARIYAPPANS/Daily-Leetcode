class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i, n, stack = 0, len(traversal), []
        while i < n:
            d = 0
            while i < n and traversal[i] == '-':
                d += 1
                i += 1
            v = 0
            while i < n and traversal[i].isdigit():
                v = v * 10 + int(traversal[i])
                i += 1
            node = TreeNode(v)
            if d == len(stack):
                if stack: stack[-1].left = node
            else:
                stack[d - 1].right = node
                stack = stack[:d]
            stack.append(node)
        return stack[0]