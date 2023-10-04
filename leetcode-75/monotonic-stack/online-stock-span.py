class StockSpanner:

    def __init__(self):
        self.day = 0
        self.stack = [(0, float('inf'))]

    def next(self, price: int) -> int:
        self.day += 1
        while self.stack[-1][1] <= price:
            self.stack.pop()
        span = self.day - self.stack[-1][0]
        self.stack.append((self.day, price))
        return span
