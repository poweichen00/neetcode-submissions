class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # newInterval 完全在目前 interval 的左邊 newInterval 已經可以確定放在這裡
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # 後面的 intervals 都不用再檢查，原本 intervals 已經排序好了
                return res + intervals[i:]
            # newInterval 完全在目前 interval 的右邊
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = (min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1]))
        # 如果迴圈跑完 newInterval 還沒被加入，代表它應該放在最後面
        res.append(newInterval)
        return res