class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        record = [0]*26

        for i in s:
            record[ord(i)-ord("a")] +=1

        for i in  t:
            record[ord(i)-ord("a")]-=1

        for i in record:
            if i != 0:
                return  False
        return True