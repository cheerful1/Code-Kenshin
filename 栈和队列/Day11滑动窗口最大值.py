from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []

        q = deque()
        result = []
        n = len(nums)

        for i in range(n):
            # 移除超出窗口的队首元素
            while q and q[0] <= i - k:
                q.popleft()

            # 维护队列的单调递减性
            while q and nums[i] >= nums[q[-1]]:
                q.pop()

            q.append(i)

            # 当窗口形成后，记录当前窗口的最大值
            if i >= k - 1:
                result.append(nums[q[0]])

        return result