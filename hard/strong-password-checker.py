class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        missing_types = 3 - sum(any(map(f, password)) for f in (str.islower, str.isupper, str.isdigit))
        if len(password) < 6:
            return max(missing_types, 6 - len(password))

        repeating = 1
        arr = [0] * 3
        for c1, c2 in zip(password[1:] + '$', password):
            if c1 == c2:
                repeating += 1
                continue
            if repeating > 2:
                arr[0] += repeating % 3 == 0
                arr[1] += repeating % 3 == 1
                arr[2] += (repeating - 2) // 3
            repeating = 1

        removable_chars = exceeding_chars = max(0, len(password) - 20)
        for i in range(3):
            removed = min(arr[i], removable_chars // (i + 1))
            arr[i] -= removed
            removable_chars -= removed * (i + 1)
        return exceeding_chars + max(missing_types, sum(arr))
