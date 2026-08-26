class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 為了模擬 Max Heap，把所有石頭重量變成負數
        stones = [-s for s in stones]
        heapq.heapify(stones)

        # 只要還有至少兩顆石頭，就繼續撞
        while len(stones) > 1:
            # 取出「最大」的石頭
            # 最小的負數代表最大的原始重量
            first = heapq.heappop(stones) 
            second = heapq.heappop(stones) 
            # first - second
            # -8 - (-7) = -1
            # -1 代表重量 1
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])