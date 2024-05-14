if __name__ == '__main__':
    n = int(input())
    count = 1
    temp = True
    stack = []
    answer = []

    for i in range(n):
        num = int(input())

        while count <= num:
            stack.append(count)
            answer.append("+")
            count += 1

        if stack[-1] == num:
            stack.pop()
            answer.append("-")
        else:
            temp = False
            break
        
    if temp == False:
        print("NO")
    else:
        for i in answer:
            print(i)