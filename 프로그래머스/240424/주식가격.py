# https://school.programmers.co.kr/learn/courses/30/lessons/42584

"""
- 스택을 활용한 문제
- O(n^2)의 문제 풀이는 시간을 초과하게 된다.
- 스택이 비어있지 않고, 이전의 가격 보다 떨이지는 경우에 연산을 통해서 가격을 확정짓는다.
- 스택 내에는 현재 시점에서 가격이 떨어지지 않은 가격만 존재하게 된다.
"""

def solution(prices):
    stack = [0]
    n = len(prices)
    answer = [0] * n

    for idx in range(1, len(prices)):
        while stack and prices[idx] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = idx - j

        stack.append(idx)

    while stack:
        j = stack.pop()
        answer[j] = n - j
    return answer

if __name__ == '__main__':
    input = [3, 2, 4, 1, 1]
    print(solution(input))