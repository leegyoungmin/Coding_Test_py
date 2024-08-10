from collections import deque 
def bfs(graph, start_v):
    q = deque()
    q.append(start_v)
    visited = [False] * len(graph)
    visited[start_v] = True

    while q:
        print(q)
        temp = q.popleft()

        if temp == 7:
            print("찾았다!!")
            return

        for el in graph[temp]:
            if visited[el] == False:
                q.append(el)
                visited[el] = True


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
bfs(graph, start_v=0)