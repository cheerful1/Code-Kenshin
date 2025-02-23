class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        slist = s.split(" ")
        return " ".join(reversed(slist))