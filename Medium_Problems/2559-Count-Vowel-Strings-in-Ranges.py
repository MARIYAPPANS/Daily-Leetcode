class Solution:
    def vowelStrings(self, w: List[str], q: List[List[int]]) -> List[int]:
        ps = [0]
        for x in w:
            ps.append(ps[-1] + (1 if x[0] in 'aeiou' and x[-1] in 'aeiou' else 0))
        
        res = []
        for r in q:
            res.append(ps[r[1] + 1] - ps[r[0]])
        
        return res
