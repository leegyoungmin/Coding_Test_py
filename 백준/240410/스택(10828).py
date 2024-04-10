import sys

def main():
    stack = []

    N = int(sys.stdin.readline())

    for _ in range(N):
        inputs = sys.stdin.readline().split()
        key = inputs[0]

        if key == "push":
            value = int(inputs[1])
            stack.append(value)
        elif key == "pop":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif key == "size":
            print(len(stack))
        elif key == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        else:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])

if __name__ == '__main__':
    main()