class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        result = [''] * numRows
        index = 0
        step = 1

        for char in s:
            result[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(result)
        

        '''P A Y P A L I S H I R  I  N  G
           0 1 2 3 4 5 6 7 8 9 10 11 12 13

           1st iter=>0   4   8    12
           2nd iter=>1 3 5 7 9 11 13
           3rd iter=>2   6   10        '''