# https://school.programmers.co.kr/learn/courses/30/lessons/12973?language=python3

def solution(s):
    stack = []

    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            last = stack[-1]

            if last == i:
                del stack[-1]
            else:
                stack.append(i)
    return 1 if len(stack) == 0 else 0

if __name__ == '__main__':
    input = input()
    result = solution(input)
    print(result)