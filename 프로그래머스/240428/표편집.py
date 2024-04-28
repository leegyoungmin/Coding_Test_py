"""
def solution(n, k, cmd):
    board = [0 for x in range(n)]
    current = k
    stack = []

    for set in cmd:
        commands = set.split(" ")
        command = commands[0]

        if command == 'D':
            m = int(commands[1])
            current += m
        elif command == 'U':
            m = int(commands[1])
            current -= m
        elif command == 'C':
            board.pop(current)
            stack.append(current)
        elif command == 'Z':
            stack.pop()
            board.append(0)

    answer = ["O" for x in range(n)]
    for s in stack:
        answer[s] = 'X'

    return "".join(answer)


if __name__ == '__main__':
    n = 8
    k = 2
    cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
    result = solution(n = n, k = k, cmd = cmd)
    print(result)
"""