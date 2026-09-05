class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # par[i] 代表節點 i 的父節點
        par = [i for i in range(n)]
        # rank[i] 代表：以 i 為 root 的這一組，目前有幾個節點
        rank = [1] * n
        def find(n1):
            # res 用來一路往上找 root
            res = n1
            # 如果 res 不是自己的 parent，就代表還沒走到 root
            while res != par[res]:
                # 讓 res 直接往上跳兩層，加快 find 的速度
                par[res] = par[par[res]]
                # 繼續往父節點走
                res = par[res]
            return res
        def union(n1, n2):
             # 找出 n1、n2 各自屬於哪一組
            p1 ,p2 = find(n1), find(n2)
            # 如果 root 一樣，代表本來就已經在同一組，不需要合併
            if p1 == p2:
                return 0
            # 把比較小的集合接到比較大的集合下面
            if rank[p2] > rank[p1]:
                # p1 接到 p2 下面
                par[p1] = p2
                # p2 這組的大小增加
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]     
            return 1
        # n 個節點 → n 組
        res = n
        # 每看到一條 edge 嘗試把兩個節點合併
        for n1, n2 in edges:
            # union 成功：union 回傳 1 component 數量就少 1
            # 原本就在同一組：union 回傳 0 component 數量不變
            res -= union(n1, n2)
        return res