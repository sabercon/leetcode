from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value, freq = self.cache[key]
        self.cache[key] = (value, freq + 1)
        self.freq_to_keys[freq + 1][key] = self.freq_to_keys[freq].pop(key, 0)
        if freq == self.min_freq and not self.freq_to_keys[freq]:
            self.min_freq += 1
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                evicted, _ = self.freq_to_keys[self.min_freq].popitem(False)
                del self.cache[evicted]
            self.min_freq = 1
            self.cache[key] = (value, 0)
        else:
            self.cache[key] = (value, self.cache[key][1])
        self.get(key)
