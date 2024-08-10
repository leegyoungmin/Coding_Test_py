from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        q.append(0)
        visited = [False] * len(rooms)
        visited[0] = True

        while q:
            temp = q.popleft()

            for element in rooms[temp]:
                if visited[element] == False:
                    q.append(element)
                    visited[element] = True
        
        return all(visited)
        
    
if __name__ == "__main__":
    sol = Solution()
    rooms = [[1],[2],[3],[]]
    res = sol.canVisitAllRooms(rooms=rooms)
    print(res)