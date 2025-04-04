class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(n):
            if not n:
                return 0, None
            l, r = dfs(n.left), dfs(n.right)
            if l[0] == r[0]:
                return l[0] + 1, n
            return (l[0] + 1, l[1]) if l[0] > r[0] else (r[0] + 1, r[1])
        return dfs(root)[1]
