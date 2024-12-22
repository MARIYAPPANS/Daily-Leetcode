class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        p = 0
        while p < len(s1) and p < len(s2) and p < len(s3):
            if s1[p] == s2[p] == s3[p]:
                p += 1
            else:
                break
        
        if p == 0:
            return -1
        
        return (len(s1) - p) + (len(s2) - p) + (len(s3) - p)
