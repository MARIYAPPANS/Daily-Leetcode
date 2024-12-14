class Solution(object):
    def addBinary(self, a, b):
        \\\
        :type a: str
        :type b: str
        :rtype: str
        \\\
       
        sum_binary = bin(int(a, 2) + int(b, 2))[2:]
        
        return sum_binary
