class Node:

    def __init__(self, key: int = 0, val: int = 0, prev: 'Node' = None, next: 'Node' = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def unlink(self) -> None:
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    def link(self, front: 'Node', back: 'Node') -> None:
        front.next = back.prev = self
        self.prev, self.next = front, back


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._add_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
        else:
            node = Node(key, value)
        self._add_tail(node)

        if len(self.cache) > self.capacity:
            self._remove_head()

    def _add_tail(self, node: Node) -> None:
        node.unlink()
        node.link(self.tail.prev, self.tail)
        self.cache[node.key] = node

    def _remove_head(self) -> None:
        node = self.head.next
        node.unlink()
        del self.cache[node.key]
