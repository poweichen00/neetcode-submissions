class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 計算每個任務出現幾次
        # ["A","A","A","B","B"] -> {"A": 3, "B": 2}
        count = Counter(tasks)
        # 所以把次數變成負數，模擬 Max Heap
        maxheap = [-n for n in count.values()]
        heapq.heapify(maxheap)
        # 紀錄目前時間
        time = 0
        # q 用來存「正在冷卻」的任務
        # [剩餘次數, 可以重新執行的時間] -> [-2, 4]
        # 這個任務還剩 2 次，到 time = 4 才能重新放回 maxHeap
        q = deque()
        # 可以執行的任務 maxHeap or 還在冷卻的任務 q
        while maxheap or q:
            time += 1
            if maxheap:
                # 拿出剩餘次數最多的任務
                cnt = 1 + heapq.heappop(maxheap)
                # 如果 cnt != 0，這個任務還沒全部做完
                if cnt:
                    # 放進冷卻 queue
                    # cnt：還剩幾次，time + n：這個任務什麼時候可以重新使用
                    q.append([cnt, time + n])

            # 檢查 queue 最前面的任務，是否冷卻完成
            if q and q[0][1] == time:
                # 冷卻完成後，把任務重新放回 maxHeap
                heapq.heappush(maxheap, q.popleft()[0])

        # 回傳完成所有任務所需要的最少時間
        return time
