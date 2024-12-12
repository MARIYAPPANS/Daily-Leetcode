class Solution(object):
    def intToRoman(self, num):
        \\\
        :type num: int
        :rtype: str
        \\\
        reference = [
            (1000, \M\),
            (900, \CM\),
            (500, \D\),
            (400, \CD\),
            (100, \C\),
            (90, \XC\),
            (50, \L\),
            (40, \XL\),
            (10, \X\),
            (9, \IX\),
            (5, \V\),
            (4, \IV\),
            (1, \I\),
        ]
        value = \\

        # Iterate through the mappings for Roman numeral construction
        for v, s in reference:
            while num >= v:
                value += s
                num -= v
        
        return value


        