class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        space_set = set(spaces)  # Convert list to set for O(1) lookups
        s1 = []
        for i in range(len(s)):
            if i in space_set:
                s1.append(" ")
            s1.append(s[i])
        return ''.join(s1)
