"""
dict = {}

def dfs(target, max_length, visited = []):
    print(target, visited, len(visited), dict)
    if len(visited) == max_length:
        value = "".join(visited)
        key = dict.get(value)
        
        if key is None:
            dict[value] = 1
        return
    
    for t in target:
        if t not in visited:
            visited.append(t)
            dfs(target, max_length, visited)
            visited.pop(0)
    
def solution(orders, course):
    answer = []
    dfs(orders[0], course[0])
    print(dict)
    return answer


if __name__ == '__main__':
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]
    result = solution(orders, course)
    print(result)
"""