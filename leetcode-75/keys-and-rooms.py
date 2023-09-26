from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)

        def dfs(room: int) -> None:
            if visited[room]:
                return
            visited[room] = True
            for key in rooms[room]:
                dfs(key)

        dfs(0)
        return all(visited)
