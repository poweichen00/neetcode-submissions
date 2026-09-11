class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        # 存目前「有可能包含 query 的區間」
        minheap = []
        # res 用來記錄每個 query 的答案
        # i 用來指向目前看到 intervals 的哪一個位置
        res, i = {}, 0
        for q in sorted(queries):
            # left <= q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                # (區間長度, 右端點)
                heapq.heappush(minheap, (r - l + 1, r))
                i += 1 
            # right < q
            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
             # heap[0][0] 就是目前最短 interval 的長度
            res[q] = minheap[0][0] if minheap else -1
        return [res[q] for q in queries]