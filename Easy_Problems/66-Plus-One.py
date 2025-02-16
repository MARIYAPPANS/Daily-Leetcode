class Solution(object):
    def plusOne(self, digits):
        \\\
        :type digits: List[int]
        :rtype: List[int]
        \\\
        d=\\
        for i in digits:
            d+=str(i)
        s=int(d)+1
        f=str(s)
        l=[]
        for i in f:
            l.append(int(i))
        return l

