# https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""
각 기능은 100%가 되는 경우에 반영이 된다.
개발 속도가 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있다.
"""

def solution(progresses, speeds):
    q = []
    p = progresses

    while len(p) != 0:
        for (idx, item) in enumerate(p):
            p[idx] += speeds[idx]

        cnt = 0

        while len(p) != 0 and p[0] >= 100:
            item = p.pop(0)
            speeds.pop(0)
            cnt += 1

        if cnt != 0:
            q.append(cnt)
    return q

if __name__ == "__main__":
    p = [95, 95, 95, 95]
    s = [4, 3, 2, 1]
    r = solution(progresses=p, speeds=s)
    print(r)