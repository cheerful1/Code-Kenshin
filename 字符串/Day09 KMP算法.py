class Solution(object):

    def strStr(self, haystack, needle):
        # 处理特殊情况：needle 为空字符串
        if not needle:
            return 0

        # 计算needle的前缀表
        lps = self.computeLPS(needle)

        i = j = 0  # i指向haystack，j指向needle
        n, m = len(haystack), len(needle)

        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                # 完整匹配时返回起始索引
                if j == m:
                    return i - j

            # 不匹配时根据前缀表回溯
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        # 未找到匹配
        return -1


    def computeLPS(self, pattern):
        """
        计算模式串的最长公共前后缀表（LPS数组）

        :param pattern: 模式串
        :return: LPS数组
        """
        m = len(pattern)
        lps = [0] * m
        length = 0  # 当前最长前缀后缀的长度

        for i in range(1, m):
            # 当前字符不匹配时，回溯到更短的前缀
            while length > 0 and pattern[i] != pattern[length]:
                length = lps[length - 1]

            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
            else:
                lps[i] = 0

        return lps