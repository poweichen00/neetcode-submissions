import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 每小時吃 1 根
        # 每小時吃完最大的一堆，再快也沒有意義，因為一小時最多只能吃一堆
        l, r = 1, max(piles)
        
        # 初始化結果為最大可能速度
        res = r
        
        # 3. 開始可行的最小速度 k
        while l <= r:
            # 猜測目前的速度 k (取中間值)
            k = (l + r) // 2
            
            # 計算以速度 k 吃完所有香蕉需要的「總小時數」
            hours = 0
            for p in piles:
                # math.ceil 是「無條件進位」(向上取整)
                # 一堆有 7 根香蕉，速度 k=3，需要 7/3 = 2.33 小時，但實際上需要 3 小時才能吃完
                hours += math.ceil(p / k)
            
            # 判斷目前的速度 k 是否可行
            if hours <= h:
                # 如果總小時數小於或等於限制時間 h，代表速度 k 是「可行」的
                res = min(res, k)  # 記錄下目前找到的最小可行速度
                r = k - 1          # 既然 k 可行，「更慢的速度」是否也可行，所以往左半邊搜尋
            else:
                # 如果總小時數大於限制時間 h，代表速度 k 「太慢了」，來不及吃完
                l = k + 1          # 必須「加快速度」，所以往右半邊搜尋
                
        return res