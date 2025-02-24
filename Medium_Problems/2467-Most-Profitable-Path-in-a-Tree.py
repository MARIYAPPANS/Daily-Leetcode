from collections import defaultdict
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Find Bob's path to the root and record the time of each visit
        bob_time = {}
        
        def find_bob_path(node, parent, time):
            bob_time[node] = time
            if node == 0:
                return True
            for neighbor in graph[node]:
                if neighbor != parent:
                    if find_bob_path(neighbor, node, time + 1):
                        return True
            del bob_time[node]
            return False
        
        find_bob_path(bob, -1, 0)
        
        # Calculate the most profitable path from the root to any leaf
        max_profit = float('-inf')
        
        def dfs(node, parent, profit, time):
            nonlocal max_profit
            if node in bob_time:
                if time == bob_time[node]:
                    profit += amount[node] // 2
                elif time > bob_time[node]:
                    profit += 0
                else:
                    profit += amount[node]
            else:
                profit += amount[node]
            
            if len(graph[node]) == 1 and node != 0:  # Leaf node
                max_profit = max(max_profit, profit)
                return
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node, profit, time + 1)
        
        dfs(0, -1, 0,0 )
        
        return max_profit