class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        size = len(nums)
        i=0
        while i < size:
            if nums[i] == val:
                for j in range(i,size-1):
                    nums[j] = nums[j+1]
                i = i - 1
                size = size - 1
            i +=1
        return size