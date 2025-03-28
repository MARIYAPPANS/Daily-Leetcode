from heapq import heappush, heappop

class Solution:
    def maxPoints(self, g: List[List[int]], q: List[int]) -> List[int]:
        r, c = len(g), len(g[0])
        res = [0] * len(q)
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Min-heap for BFS
        pq = [(g[0][0], 0, 0)]  # (value, row, col)
        vis = [[False] * c for _ in range(r)]
        vis[0][0] = True
        
        tp = 0  # Total points
        cur_max = 0  # Current max query value processed
        
        # Sort queries by value but keep track of their indices
        sq = sorted((v, i) for i, v in enumerate(q))
        idx = 0  # Index for sorted queries
        
        while pq:
            # Expand cells until the heap is empty or all queries are processed
            cv, cr, cc = heappop(pq)
            
            # Process queries up to the current cell value
            while idx < len(sq) and sq[idx][0] <= cv:
                res[sq[idx][1]] = tp
                idx += 1
            
            # Increment total points for the current cell
            tp += 1
            
            # Explore neighbors
            for ro, co in DIRS:
                nr, nc = cr + ro, cc + co
                if 0 <= nr < r and 0 <= nc < c and not vis[nr][nc]:
                    heappush(pq, (g[nr][nc], nr, nc))
                    vis[nr][nc] = True
        
        # Process remaining queries
        while idx < len(sq):
            res[sq[idx][1]] = tp
            idx += 1
        
        return res
