class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # 保留下來的上一個 interval 的結束位置
        preend = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            # 沒有重疊
            if start >= preend:
                # 把 preend 更新成現在的 end
                preend = end
            else:
                res += 1
                # 保留比較早結束的 interval
                # 因為越早結束，後面越容易接更多 interval
                preend = min(preend, end)
        return res