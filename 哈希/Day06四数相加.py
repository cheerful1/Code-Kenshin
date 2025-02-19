class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """

        ab_map = {}
        cd_res = list()
        r = 0
        for i in nums1:
            for j in nums2:
                target = i+j
                ab_map[target] = ab_map.get(target,0)+1

        for k in nums3:
            for t in nums4:
                cd_res.append(0-(k+t))

        for sum in cd_res:
            if ab_map.get(sum,0)!=0:
                r+=ab_map.get(sum,0)

        return r