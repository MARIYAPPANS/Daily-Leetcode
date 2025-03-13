class Solution:
    def minZeroArray(self,A: List[int],Q: List[List[int]])->int:
        n=len(A)
        def chk(k):
            D=[0]*(n+1)
            for i in range(k):
                l,r,v=Q[i]
                D[l]+=v
                D[r+1]-=v
            c=0
            for i in range(n):
                c+=D[i]
                if c<A[i]:return 0
            return 1
        if all(x==0 for x in A):return 0
        l,r=1,len(Q)
        if not chk(r):return -1
        while l<r:
            m=(l+r)//2
            if chk(m):r=m
            else:l=m+1
        return l
