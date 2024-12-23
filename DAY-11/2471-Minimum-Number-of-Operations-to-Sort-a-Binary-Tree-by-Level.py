from collections import deque

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def min_swaps(arr):
            idx_map = {v: i for i, v in enumerate(sorted(arr))}
            visited = [False] * len(arr)
            swaps = 0

            for i in range(len(arr)):
                if visited[i] or idx_map[arr[i]] == i:
                    continue

                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = idx_map[arr[j]]
                    cycle_size += 1

                if cycle_size > 1:
                    swaps += cycle_size - 1

            return swaps

        queue = deque([root])
        operations = 0

        while queue:
            level_values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            operations += min_swaps(level_values)

        return operations
