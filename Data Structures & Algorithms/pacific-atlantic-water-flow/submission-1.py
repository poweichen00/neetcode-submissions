class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        # pac：可以流到 Pacific 的格子
        # atl：可以流到 Atlantic 的格子
        pac, atl = set(), set()
        def dfs(r, c, visit, prevheight):
            # 目前高度比上一格還低
            if (r < 0 or r == rows or c < 0 or c == cols or (r, c) in visit or heights[r][c] < prevheight):
                return 
            visit.add((r, c))
            # 往四個方向繼續 DFS，把目前高度當成下一步的 prevheight
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        # 左邊界屬於 Pacific 右邊界屬於 Atlantic
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])
        # 上邊界屬於 Pacific 下邊界屬於 Atlantic
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res