class Node:

    def __init__(self, key: int = 0, val: int = 0, freq: int = 0, prev: 'Node' = None, next: 'Node' = None):
        self.key = key
        self.val = val
        self.freq = freq
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


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node: dict[int, Node] = {}
        self.freq_to_node: dict[int, Node] = {0: Node(next=Node())}

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._use(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
        else:
            if len(self.key_to_node) + 1 > self.capacity:
                self._evict_lfu()
            node = Node(key, value, 0)
            self.key_to_node[key] = node
        self._use(node)

    def _use(self, node: Node):
        old_freq = node.freq
        new_freq = node.freq = node.freq + 1
        if new_freq in self.freq_to_node:
            front = self.freq_to_node[new_freq]
        elif self.freq_to_node[old_freq] != node:
            front = self.freq_to_node[old_freq]
        else:
            front = node.prev
        if self.freq_to_node[old_freq] == node:
            del self.freq_to_node[old_freq]
            if node.prev.freq == old_freq:
                self.freq_to_node[old_freq] = node.prev
        self.freq_to_node[new_freq] = node
        node.unlink()
        node.link(front, front.next)

    def _evict_lfu(self):
        evicted = self.freq_to_node[0].next
        evicted.unlink()
        del self.key_to_node[evicted.key]
        if self.freq_to_node[evicted.freq] == evicted:
            del self.freq_to_node[evicted.freq]
