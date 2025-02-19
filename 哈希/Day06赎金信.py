class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        res_dict = dict()
        for m in magazine:
            res_dict[ord(m)-ord("a")] = res_dict.get(ord(m)-ord("a"),0)+1
        for r in ransomNote:
            if res_dict.get(ord(r)-ord("a")) <= 0:
                return False
            else:
                res_dict[ord(r)-ord("a")] -= 1

        return  True