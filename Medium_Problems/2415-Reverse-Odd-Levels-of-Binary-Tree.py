# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        queue = deque([root])
        level = 0
        
        while queue:
            n = len(queue)
            if level % 2 == 1:
                values = [node.val for node in queue]
                for i in range(n):
                    queue[i].val = values[n - i - 1]
            
            for _ in range(n):
                node = queue.popleft()
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            
            level += 1
        
        return root
