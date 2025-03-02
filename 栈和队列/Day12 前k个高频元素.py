class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #对频率排序
        #定义一个小顶堆，大小为k
        smap = {}
        for i in range(len(nums)):
            smap[nums[i]] = smap.get(nums[i],0)+1

        # #用固定大小为k的小顶堆，扫描所有频率的数值
        xiao_que = []

        for key,freq in smap.items():
            heapq.heappush(xiao_que,(freq,key))
            if len(xiao_que) > k:  # #如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(xiao_que)

        #找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = []
        while xiao_que:
            result.append(heapq.heappop(xiao_que)[1])
        result.reverse()
        return result
