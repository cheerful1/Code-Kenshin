# 106.从中序与后序遍历序列构造二叉树
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # 第一步: 特殊情况讨论: 树为空. (递归终止条件)
        if not postorder:
            return None
        # 第二步: 后序遍历的最后一个就是当前的中间节点.
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 第三步: 找切割点.index函数的应用！
        sparator_idx = inorder.index(root_val)

        # 第四步: 切割inorder数组. 得到inorder数组的左,右半边.
        inorder_left = inorder[:sparator_idx]
        inorder_right = inorder[sparator_idx + 1:]

        # 第五步: 切割postorder数组. 得到postorder数组的左,右半边.
        # ⭐️ 重点1: 中序数组大小一定跟后序数组大小是相同的.
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left): len(postorder) - 1]

        # 第六步: 递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root


# 654.最大二叉树
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
        # max_num = -1
        # max_index = -1
        #
        # for num in nums:
        #     if num > max_num:
        #         max_index = nums.index(num)
        #         max_num = nums[max_index]
        max_num = max(nums)
        max_index = nums.index(max_num)

        root = TreeNode(max_num)
        # 分割左区间，一定保证有一个元素
        if max_index > 0:
            root.left = self.constructMaximumBinaryTree(nums[:max_index])
        if max_index < len(nums) - 1:
            root.right = self.constructMaximumBinaryTree(nums[max_index+1:])


        # root.left = self.constructMaximumBinaryTree(nums[:max_index])
        # root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return root

# 617.合并二叉树
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        root = TreeNode(None)
        if not root1:
            return root2
        if not root2:
            return root1
        root.val = root1.val + root2.val
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root