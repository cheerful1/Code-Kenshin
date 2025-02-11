class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        nums = [[0] * n for _ in range(n)]

        startx = 0
        starty = 0

        loop = n // 2
        mid = n // 2

        count = 1  # 用来计数

        for offset in range(1, loop + 1):
            for i in range(starty, n - offset):
                nums[startx][i] = count  # 从左到右，主要是第二个左边变化
                count += 1
            for i in range(startx, n - offset):
                nums[i][n - offset] = count  # 从上到下，startx=0,主要是第一个坐标变化 
                count += 1
            for i in range(n - offset, startx, -1): # 从右到左，第一个坐标不变，变的是第二个左边
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, starty, -1): #从下到上，主要是第一个坐标变化，第二个左边不变
                nums[i][starty] = count   # 
                count += 1
            startx += 1
            starty += 1

        if n % 2 != 0:
            nums[mid][mid] = count
        return nums


if __name__ == "__main__":
    n = 3  # 定义矩阵大小
    solution = Solution()  # 创建类的实例
    result = solution.generateMatrix(n)  # 调用方法

    # 打印结果
    for row in result:
        print(row)