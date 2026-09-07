"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i: i.start)
        minheap = []
        for interval in intervals:
            # 如果目前會議開始時，最早結束的那間房已經空出來
            if minheap and minheap[0] <= interval.start:
                heapq.heappop(minheap)
            # 把目前會議的結束時間放進 heap
            heapq.heappush(minheap, interval.end)
        # heap 最後有幾個結束時間，就代表最多同時需要幾間房
        return len(minheap)