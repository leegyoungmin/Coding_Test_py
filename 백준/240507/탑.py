"""
N개의 높이가 다른 탑을 왼쪽에서 오른쪽으로 세운다.
하나의 탑에서 발사된 신호는 가장 먼저 나오는 탑에서 수신이 가능하다.

반복문에서 스택에 쌓인 놈들 중에 자신보다 큰 놈의 개수를 찾는다.
"""

import sys

input = sys.stdin.readline

n = int(input())
tops = list(map(int,input().split()))
answer= [0] * n
stack = []

#가장 먼저 만나는 높이가 같거나 큰 탑에서 수신가능
for i in range(len(tops)):
    while stack:
        if tops[stack[-1][0]]<tops[i]:
            stack.pop()
        else:
            answer[i] = stack[-1][0]+1
            break
    stack.append((i,tops[i]))
    
print(*answer)