import random
from collections import defaultdict


class RandomizedCollection:

    def __init__(self):
        self.num_dict = defaultdict(set)
        self.num_list = []

    def insert(self, val: int) -> bool:
        self.num_dict[val].add(len(self.num_list))
        self.num_list.append(val)
        return len(self.num_dict[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.num_dict[val]:
            return False
        i = self.num_dict[val].pop()
        last = self.num_list.pop()
        if i < len(self.num_list):
            self.num_dict[last].remove(len(self.num_list))
            self.num_dict[last].add(i)
            self.num_list[i] = last
        return True

    def getRandom(self) -> int:
        return random.choice(self.num_list)
