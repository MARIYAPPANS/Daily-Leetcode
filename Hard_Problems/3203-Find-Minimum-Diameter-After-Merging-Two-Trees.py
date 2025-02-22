class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        from collections import defaultdict, deque

        def calculate_diameter(edges):
            if not edges:  # Handle empty edge list
                return 0
            
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            def bfs(node):
                visited = set()
                queue = deque([(node, 0)])
                visited.add(node)
                farthest_node, max_dist = node, 0
                while queue:
                    current, dist = queue.popleft()
                    if dist > max_dist:
                        max_dist, farthest_node = dist, current
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append((neighbor, dist + 1))
                return farthest_node, max_dist

            start_node = next(iter(graph.keys()))
            farthest_node, _ = bfs(start_node)
            _, diameter = bfs(farthest_node)
            return diameter

        # Calculate diameters of both trees
        diameter1 = calculate_diameter(edges1)
        diameter2 = calculate_diameter(edges2)

        # Connect two trees with an edge to minimize the overall diameter
        return max(diameter1, diameter2, (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1)
