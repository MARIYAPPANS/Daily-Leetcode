class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        def build(ps, pe, po_s):
            if ps > pe: return None
            if ps == pe: return TreeNode(pre[ps])
            l = pre[ps + 1]
            n = 1
            while post[po_s + n - 1] != l: n += 1
            r = TreeNode(pre[ps])
            r.left = build(ps + 1, ps + n, po_s)
            r.right = build(ps + n + 1, pe, po_s + n)
            return r
        return build(0, len(pre) - 1, 0)
