from collections import deque


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def remove_consecutive(row: str, index: int, inserted: str) -> str:
            if inserted != row[index] or row[index] != row[index + 1]:
                return row[:index] + inserted + row[index:]

            left, right = index - 1, index + 2
            while row[left] != '^' and row[right] != '$':
                color = row[left]
                new_left, new_right = left - 1, right
                while row[new_left] == color:
                    new_left -= 1
                while row[new_right] == color:
                    new_right += 1
                if left - new_left + new_right - right < 3:
                    break
                left, right = new_left, new_right

            return row[:left + 1] + row[right:]

        board = '^' + board + '$'
        queue = deque([(board, hand, 0)])
        seen = {(board, hand)}
        while queue:
            board, hand, steps = queue.popleft()
            for i, h in enumerate(hand):
                new_hand = hand[:i] + hand[i + 1:]
                for j in range(1, len(board) - 1):
                    if h == board[j - 1] or (h != board[j] and board[j] != board[j - 1]):
                        continue
                    new_board = remove_consecutive(board, j, h)
                    if new_board == '^$':
                        return steps + 1
                    if (new_board, new_hand) not in seen:
                        seen.add((new_board, new_hand))
                        queue.append((new_board, new_hand, steps + 1))
        return -1
