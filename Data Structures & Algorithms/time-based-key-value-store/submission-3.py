class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, value = "", self.store.get(key, [])
        l, r = 0, len(value)-1
        while l <= r:
            m = (l + r) // 2
            # 因為我們要找的是「小於等於目標值的最大值」
            # 即使現在這個符合條件，還是要嘗試往右找更大的 timestamp 找找看，有沒有更接近目標 timestamp 的值。
            if value[m][1] <= timestamp:
                res = value[m][0]
                l = m + 1 
            # 目前的 timestamp 太大了 (大於目標)
            # 必須往左邊找更小的 timestamp。
            else:
                r = m - 1
        return res