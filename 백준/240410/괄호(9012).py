import sys

def makeValues(values):
    stack = []

    for value in values:
        if len(stack) == 0:
            stack.append(value)
        else:
            last = stack[-1]

            if last == "(" and value == ")":
                stack.pop()
            else:
                stack.append(value)

    return len(stack) == 1

def main():
    T = int(sys.stdin.readline())

    for _ in range(T):
        input = sys.stdin.readline()

        if makeValues(input):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()