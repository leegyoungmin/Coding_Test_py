"""
인덴트를 고치려고한다. 각 줄은 탭키를 사용했다.
연속된 줄을 그룹으로 선택하고, 각 줄의 앞에 탭을 추가하거나, 삭제할 수 있다.

N의 개수와 앞에 있는 탭의 개수와 올바른 탭의 개수를 준다.
한번 편집할 때, 다음과 같이 명령을 수행할 수 있다.

- 연속된 줄을 그룹으로 선택
- 선택된 줄 앞에 탭을 1개 추가하거나 삭제할 수 있다.
"""

"""
if __name__ == '__main__':
    n = int(input())
    currents = list(map(int, input().split(" ")))
    targets = list(map(int, input().split(" ")))

    items = []
    cnt = 0

    for idx in range(len(currents)):
        item = currents[idx] - targets[idx]
        items.append(item)

    while True:
        stack = []
        is_upper = True

        for idx in range(len(items)):
            if items[idx] == 0:
                continue

            if len(stack) == 0:
                is_upper = (items[idx] > 0)
                stack.append(idx)
                continue
            else:
                if is_upper == True and items[idx] > 0:
                    stack.append(idx)
                elif is_upper == False and items[idx] < 0:
                    stack.append(idx)
                else:
                    break
        
        if len(stack) == 0:
            break

        for jdx in stack:
            if is_upper:
                items[jdx] -= 1
            else:
                items[jdx] += 1
        cnt += 1
    
    print(cnt)
"""