class Node:

    def __init__(self, key: str, val: int, prev: 'Node' = None, next: 'Node' = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def link(self, prev: 'Node', next: 'Node'):
        prev.next = next.prev = self
        self.prev, self.next = prev, next

    def unlink(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def move_forward(self) -> None:
        while self.val > self.next.val:
            self.prev.next = self.next
            self.next.prev = self.prev
            self.prev = self.next
            self.next = self.next.next
            self.prev.next = self.next.prev = self

    def move_back(self) -> None:
        while self.val < self.prev.val:
            self.next.prev = self.prev
            self.prev.next = self.next
            self.next = self.prev
            self.prev = self.prev.prev
            self.next.prev = self.prev.next = self


class AllOne:

    def __init__(self):
        self.key_to_node = {}
        self.head = Node('', -1)
        self.tail = Node('', 2 ** 31 - 1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key not in self.key_to_node:
            node = Node(key, 1)
            node.link(self.head, self.head.next)
            self.key_to_node[key] = node
        else:
            self.key_to_node[key].val += 1
            self.key_to_node[key].move_forward()

    def dec(self, key: str) -> None:
        if self.key_to_node[key].val == 1:
            self.key_to_node.pop(key).unlink()
        else:
            self.key_to_node[key].val -= 1
            self.key_to_node[key].move_back()

    def getMaxKey(self) -> str:
        return self.tail.prev.key

    def getMinKey(self) -> str:
        return self.head.next.key
