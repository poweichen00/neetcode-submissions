"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}

        def dfs(node):
            # 如果這個舊節點已經複製過，直接回傳對應的新節點
            if node in oldtonew:
                return oldtonew[node]
            # 建立新的節點
            copy = Node(node.val)
            # 立刻記錄 舊節點 -> 新節點
            oldtonew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None