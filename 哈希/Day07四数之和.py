class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = list()
        nums.sort()

        for k in range(len(nums)-3):
            # 1、跳过重复的k
            if k>0 and nums[k] ==nums[k-1]:
                continue
            # 2、剪枝：3若当前最小和已超过target，无需继续
            if nums[k] + nums[k+1] + nums[k+2]+nums[k+3]>target:break

            for i in  range(k+1,len(nums)-2):
                # 3、剪枝：跳过重复的i
                if i>k+1 and nums[i] == nums[i-1]:continue

                left = i+1
                right = len(nums) - 1
                while left < right:
                    if nums[k] + nums[i] + nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[k] + nums[i] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        result.append([nums[k],nums[i],nums[left],nums[right]])
                        while left< right and nums[left] == nums[left+1]: left+=1
                        while left<right and nums[right] == nums[right-1]: right-=1
                        left += 1
                        right -= 1
        return result