class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 定义
        result = []
        nums.sort()
        # 遍历
        for i in range(len(nums)):
            if nums[i] > 0: break
            if i>0 and nums[i] == nums[i-1]: continue
            left = i+1
            right = len(nums)-1
            while(right>left):
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while  right>left and nums[right] == nums[right-1]: right -= 1
                    while  right>left and nums[left] == nums[left+1]: left += 1
                    left += 1
                    right -= 1
        return result