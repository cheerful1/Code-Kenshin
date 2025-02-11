class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        min_len = float('inf')
        size = len(nums)
        sum = 0

        while right < size:
            sum += nums[right]
            while sum >= target:
                min_len = min(min_len, right - left+1)
                sum = sum - nums[left]
                left += 1
            right += 1
        return min_len if min_len != float('inf') else 0