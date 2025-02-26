class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        que = deque()
        slist  = list(s)

        for i in range(len(slist)):
            if slist[i] == "(":
                que.append(")")
            elif slist[i] == "{":
                que.append("}")
            elif slist[i] == "[":
                que.append("]")
            elif not que or que[-1] != slist[i]:
                return False
            else:
                que.pop()

        return True if not que else False