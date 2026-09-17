class MedianFinder:

    def __init__(self):
        # small：存「較小的一半」Max Heap
        # large：存「較大的一半」Min Heap
        self.small, self.large = [], []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        # small 最大值 > large 最小值代表放錯邊了
        if self.small and self.large and ( -1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # 如果 small 比 large 多超過 1 個元素
        if len(self.small) > len(self.large)+1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small)+1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # 如果 small 比 large 多一個
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        # small 最大值 和 large 最小值 的平均   
        return (-1 * self.small[0] + self.large[0]) / 2
        