class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.maxDepthHelper(root)

    def maxDepthHelper(self, root):
        if not root:
            return 0
        left = self.maxDepthHelper(root.left)
        right = self.maxDepthHelper(root.right)
        return 1 + max(left, right)