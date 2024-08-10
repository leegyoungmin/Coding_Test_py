def dfs(cur_v):
    visited[cur_v] = True

    for next in graph[cur_v]:
        if next not in visited:
            dfs(next)

# visited dictionary version
visited = {}
# visited list version
graph = {
    0: [1, 3, 6],
    1: [0, 3],
    2: [3],
    3: [0, 1, 2, 7],
    4: [5],
    5: [4, 6, 7],
    6: [0, 5],
    7: [3, 5],
}
dfs(0)