class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        tiles = ''.join(sorted(tiles))
        
        def dfs(path, t):
            if path:
                res.add(path)
            for i in range(len(t)):
                if i > 0 and t[i] == t[i - 1]:
                    continue
                dfs(path + t[i], t[:i] + t[i+1:])
        
        dfs('', tiles)
        return len(res)