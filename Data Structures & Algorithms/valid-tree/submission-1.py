class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n :
            return True
        # adj[i] = 跟節點 i 相連的所有節點
        # edges = [[0,1], [0,2]]
        # adj = { 0: [1,2], 1: [0], 2: [0]}
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1) 
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                # 如果這個鄰居就是「上一個節點」，不算 cycle，直接跳過，這只是原路回去
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        return dfs(0, -1) and n == len(visit)