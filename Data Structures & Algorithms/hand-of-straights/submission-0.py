class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        minheap = list(count.keys())
        heapq.heapify(minheap)
        while minheap:
            first = minheap[0]
            for i in range(first, first + groupSize):
                # 如果中間缺少任何一個連續數字
                if i not in count:
                    return False
                # 使用掉一張 i
                count[i] -= 1
                # 如果 i 已經用完，也必須剛好是 heap 中最小的牌
                if count[i] == 0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)
        return True