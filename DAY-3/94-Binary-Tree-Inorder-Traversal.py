# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: List[int]
        \\\
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Traverse to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Backtrack to the most recent node
            current = stack.pop()
            result.append(current.val)  # Visit the node
            
            # Move to the right subtree
            current = current.right
        
        return result
