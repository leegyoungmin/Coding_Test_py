from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(item) for item in grid]

        def find_island(y: int, x: int):
            x_axis, y_axis = [1, -1, 0, 0], [0, 0, 1, -1]
            q = []
            q.append((y, x))
            visited[y][x] = True

            while len(q) != 0:
                tmp = q.pop(0)
                y, x = tmp[0], tmp[1]

                for idx in range(4):
                    x_alpha, y_alpha = x_axis[idx], y_axis[idx]
                    xp, yp = x + x_alpha, y + y_alpha

                    if xp < 0 or yp < 0 or xp >= len(grid[y]) or yp >= len(grid): continue;
                    if visited[yp][xp]: continue;
                    if grid[yp][xp] == "1":
                        q.append((yp, xp))
                        visited[yp][xp] = True

        cnt = 0

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "1" and visited[y][x] == False:
                    find_island(y = y, x = x)
                    cnt += 1


        return cnt
        

if __name__ == "__main__":
    sol = Solution()

    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    print(sol.numIslands(grid=grid))