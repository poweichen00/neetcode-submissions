class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        # 最後的修課順序
        output = []
        # visit：已經完整檢查過，而且確認沒問題的課
        # cycle：目前這條 DFS 路徑上正在檢查的課
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            # 如果這門課以前已經完整檢查過，代表它一定沒問題，不需要再 DFS
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return output