from collections import defaultdict
from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        total_components = 0

        def dfs(node, parent):
            nonlocal total_components
            total_sum = values[node]
            for neighbor in tree[node]:
                if neighbor != parent:
                    subtree_sum = dfs(neighbor, node)
                    if subtree_sum % k == 0:
                        total_components += 1
                    else:
                        total_sum += subtree_sum
            return total_sum

        total_sum = dfs(0, -1)
        if total_sum % k != 0:
            return 0
        return total_components + 1
