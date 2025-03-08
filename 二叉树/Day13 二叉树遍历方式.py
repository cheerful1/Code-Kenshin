class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        res = list()
        preorder(root)
        return res


# 后序遍历
class Solution:
    def postorder(self, root):
        ans = []
        def dfs(node):
            if node is None:
                return
            for ch in node.children: # 先递归处理所有子节点
                dfs(ch)
            ans.append(node.val)
        dfs(root)
        return ans

# 中序遍历
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        res = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res