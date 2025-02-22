class Solution:
    def isPalindrome(self, s: str) -> bool:
        snew = \\
        for i in s:
            if i.isalnum():  # Keep only alphanumeric characters
                snew += i.lower()  # Convert to lowercase
        return snew == snew[::-1]  # Check if the string is equal to its reverse
