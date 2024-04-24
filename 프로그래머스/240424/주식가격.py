# https://school.programmers.co.kr/learn/courses/30/lessons/42584

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