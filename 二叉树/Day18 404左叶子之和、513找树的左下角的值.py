# 左叶子之和
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0

        leftnum = self.sumOfLeftLeaves(root.left)
        if root.left is not None and root.left.left is None and root.left.right is None:
            leftnum = root.left.val
        rightnum = self.sumOfLeftLeaves(root.right)
        sum = leftnum + rightnum
        return sum



class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        self.max_depth = -1
        self.result = None

        self.dfs(root, 0)
        return self.result

    def dfs(self, node, depth):
        if not node:
            return

        if node.left:
            self.dfs(node.left, depth + 1)

        if depth > self.max_depth:
            self.max_depth = depth
            self.result = node.val

        if node.right:
            self.dfs(node.right, depth + 1)



class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        return self.hasPathSum2(root, targetSum - root.val)

    def hasPathSum2(self, cur, targetSum):

        if not cur.left and not cur.right and targetSum == 0: # 遇到叶子节点，并且计数为0
            return True
        if not cur.left and not cur.right and targetSum != 0: # 遇到叶子节点直接返回
            return False
        if cur.left:
            targetSum -= cur.left.val
            if self.hasPathSum2(cur.left, targetSum):
                return True
            targetSum += cur.left.val

        if cur.right:
            targetSum -= cur.right.val
            if self.hasPathSum2(cur.right, targetSum):
                return True
            targetSum += cur.right.val
        return False