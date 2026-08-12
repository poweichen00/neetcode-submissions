class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.pre = None
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.pre = self.right, self.left
    def remove(self, node):
        pre, nxt = node.pre, node.next
        pre.next, nxt.pre = nxt, pre
    def insert(self, node):
        pre, nxt = self.right.pre, self.right
        pre.next = nxt.pre = node
        node.next, node.pre = nxt, pre

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]