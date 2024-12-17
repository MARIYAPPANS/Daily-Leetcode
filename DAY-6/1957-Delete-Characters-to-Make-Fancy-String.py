class Solution:
    def makeFancyString(self, s: str) -> str:
        snew = s[0]  # Start with the first character
        count = 1  # Count consecutive occurrences of the current character
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            
            if count < 3:
                snew += s[i]
        
        return snew
