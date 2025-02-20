class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        size = len(s)
        j = len(s)-1
        for i in range(size//2):
            s[i], s[j] = s[j],s[i]
            j-=1