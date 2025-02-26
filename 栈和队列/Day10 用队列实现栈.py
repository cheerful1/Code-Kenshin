from collections import deque


class MyStack(object):

    def __init__(self):
        self.que = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.que.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None

        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self):
        """
        :rtype: int
        """
        # 获取栈顶的元素
        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())
        temp = self.que.popleft()
        self.que.append(temp)
        return temp

    def empty(self):
        """
        :rtype: bool
        """
        return not self.que