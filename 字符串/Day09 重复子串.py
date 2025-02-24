class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newstr = s + s
        if newstr[1:len(newstr)-1].count(s):
            return True
        return False