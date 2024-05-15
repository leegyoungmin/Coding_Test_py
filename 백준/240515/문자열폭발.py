"""
문자열에 폭발 문자열을 심음
폭발 문자열이 폭발하면 문자는 사라지고, 남은 문자열은 합쳐진다.

- 문자열을 포함하고 있으면, 모든 폭발 문자열은 폭발하게 된다.
- 남은 문자열은 모여서 새로운 문자열이 된다.
- 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수 있다.
- 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
"""

def check_items(stack, bomb):
    stack = stack
    slicing = "".join(stack[-len(bomb):])

    if slicing == bomb:
        for _ in range(len(bomb)):
            stack.pop()
    return stack

if __name__ == '__main__':
    targets = list(input())
    bomb = input()

    stack = []

    for t in targets:
        if len(stack) == 0:
            stack.append(t)
        else:
            if len(stack) >= len(bomb):
                stack = check_items(stack = stack, bomb = bomb)

            stack.append(t)

    stack = check_items(stack=stack, bomb=bomb)

    if len(stack) == 0:
        print("FRULA")
    else:
        print("".join(stack))

    