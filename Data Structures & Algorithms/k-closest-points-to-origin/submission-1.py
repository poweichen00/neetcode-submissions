class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 存 [距離, x, y]
        minheap = []
        for x, y in points:
            # sqrt(x^2 + y^2)，因為比較大小不需要真的開根號
            # 直接用 x^2 + y^2 就可以
            dist = (x ** 2) + (y ** 2)
            minheap.append([dist, x, y])

        # 距離最小的元素會在最前面
        heapq.heapify(minheap)
        res = []
        # k 代表「還要取幾個最近的點」
        while k > 0:
            dist, x, y = heapq.heappop(minheap)
            res.append([x, y])
            k -= 1
        return res