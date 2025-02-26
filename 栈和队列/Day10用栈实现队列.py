class MyQueue(object):

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self):
        """
        :rtype: bool
        """
        if not self.stack_out and not self.stack_in:
            return True
        return False