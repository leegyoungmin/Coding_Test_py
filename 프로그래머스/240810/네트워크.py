def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(cur_x):
        visited[cur_x] = True

        for jdx in range(len(computers[cur_x])):
            if jdx == cur_x: continue

            if visited[jdx] == False and computers[cur_x][jdx] == 1:
                dfs(jdx)
    
    for idx in range(n):
        if visited[idx] == False:
            dfs(idx)
            answer += 1
    
    return answer