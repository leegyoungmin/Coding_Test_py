# https://www.acmicpc.net/problem/1158

# My Solution
"""
NK = input().split(" ")
n = int(NK[0])
k = int(NK[1])

q = list(range(1, n + 1))

result = []
front = 1

while len(result) < n:
    temp = q.pop(0)

    if front % k == 0 and front != 0:
        result.append(temp)
    else:
        q.append(temp)
    
    front += 1

print('<', end='')
for idx in range(len(result)):
    if idx != n - 1:
        print(f'{result[idx]}, ', end="")
    else:
        print(f'{result[idx]}', end="")
print(">", end="")
"""