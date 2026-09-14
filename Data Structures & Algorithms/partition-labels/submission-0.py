class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 字元最後一次出現的位置
        lastindex = {}
        for i, c in enumerate(s):
            lastindex[c] = i
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            # 所以這一段至少要延伸到它最後一次出現的位置
            end = max(end, lastindex[c])
            # 如果目前 index 已經走到 end
            if i == end:
                res.append(size)
                size = 0
        return res
