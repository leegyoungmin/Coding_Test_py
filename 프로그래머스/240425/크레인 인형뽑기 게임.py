"""
- Moves에 있는 값은 뽑을 수 있는 것이 된다. 그렇다면, 배열을 돌면서, 0이 아닌 곳이 나올 때까지 loop를 돌고
나오면 뽑아낸 후, 0으로 변경

- 뽑은 인형은 stack 구조에 담아서 마지막 값과 2개가 같은 경우 사라지게 한다.
- 사라지는 경우, 인형은 2씩 증가한다.
"""

def solution(board, moves):
    stack = []
    answer = 0

    for c in moves:
        for r in range(len(board)):
            if board[r][c - 1] != 0:
                item = board[r][c - 1]
                board[r][c - 1] = 0

                if len(stack) == 0:
                    stack.append(item)
                else:
                    last = stack[-1]

                    if last == item:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(item)
                
                break

    return answer

if __name__ == '__main__':
    boards = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    result = solution(board = boards, moves = moves)
    print(result)