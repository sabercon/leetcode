import random


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.num_index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.num_index_map:
            return False
        self.nums.append(val)
        self.num_index_map[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Uses swap to remove the element in O(1) time.
        """

        if val not in self.num_index_map:
            return False
        idx = self.num_index_map.pop(val)
        last = self.nums.pop()
        if idx != len(self.nums):
            self.nums[idx] = last
            self.num_index_map[last] = idx
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
