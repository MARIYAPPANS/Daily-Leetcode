class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split()
        for i, word in enumerate(words):
            if word.startswith(searchWord):  # Check if searchWord is a prefix of the word
                return i + 1  # Return 1-based index
        return -1
