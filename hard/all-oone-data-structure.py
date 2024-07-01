from typing import Set, Dict


class Node:

    def __init__(self, count: int, keys: Set[str], prev: 'Node' = None, next: 'Node' = None):
        self.count = count
        self.keys = keys
        self.prev = prev
        self.next = next

    def link(self, prev: 'Node', next: 'Node'):
        prev.next = next.prev = self
        self.prev, self.next = prev, next

    def unlink(self):
        self.prev.next = self.next
        self.next.prev = self.prev


class AllOne:

    def __init__(self):
        self.key_to_node: Dict[str, Node] = {}
        self.head = Node(0, {''})
        self.tail = Node(0, {''})
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key in self.key_to_node:
            current = self.key_to_node[key]
            current.keys.remove(key)
        else:
            current = self.head
        if current.next.count != current.count + 1:
            node = Node(current.count + 1, set())
            node.link(current, current.next)
        else:
            node = current.next
        node.keys.add(key)
        self.key_to_node[key] = node
        if not current.keys:
            current.unlink()

    def dec(self, key: str) -> None:
        current = self.key_to_node[key]
        current.keys.remove(key)
        if current.prev.count != current.count - 1:
            node = Node(current.count - 1, set())
            node.link(current.prev, current)
        else:
            node = current.prev
        if node.count > 0:
            node.keys.add(key)
            self.key_to_node[key] = node
        else:
            del self.key_to_node[key]
        if not current.keys:
            current.unlink()

    def getMaxKey(self) -> str:
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        return next(iter(self.head.next.keys))
