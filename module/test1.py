import heapq

heap = [1, 3, 5, 7]
heapq.heappush(heap, 2)  # 确保了堆的顺序性
print(heap) # 输出: [1, 3, 2, 7, 5]