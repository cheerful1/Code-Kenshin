class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for char in tokens:
            if char in '+-*/':
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if char == '+':
                    stack.append(num2 + num1)
                elif char == '-':
                    stack.append(num2 - num1)
                elif char == '*':
                    stack.append(num2 * num1)
                elif char == '/':
                    # 处理除法，向零取整
                    stack.append(int(num2 / num1))
            else:
                stack.append(int(char))
        return stack.pop()