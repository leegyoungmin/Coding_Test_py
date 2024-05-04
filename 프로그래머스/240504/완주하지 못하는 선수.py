"""
한명의 선수를 제외하고 모든 선수가 마라톤 완주
완주하지 못한 선수의 이름을 return
"""

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for (p, c) in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

if __name__ == '__main__':
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    result = solution(participant=participant, completion=completion)
    print(result)