class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.s = set()
        def dfs(node, v):
            if not node: return
            node.val = v
            self.s.add(v)
            dfs(node.left, 2*v+1)
            dfs(node.right, 2*v+2)
        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.s
