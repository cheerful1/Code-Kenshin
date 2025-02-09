class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r, i = 0, len(nums) - 1, len(nums) - 1
        res = [float('inf')] * len(nums)

        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2:
                res[i] = nums[r] ** 2
                r -= 1
            else:
                res[i] = nums[l] ** 2
                l+=1 # 指针往右移动
            i-=1 # 存放结果的指针需要往前平移一位
        return res
