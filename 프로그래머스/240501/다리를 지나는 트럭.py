"""
트럭이 일차선 다리를 정해진 순으로 건넌다.
모든 트럭이 다리를 건너려면 최소 몇초 걸리는 지 알고 싶다.
트럭이 최대 bridge Length 만큼 올라갈 수 있다.
weight 무게 이하까지만 버틸 수 있다.

시간이 지남에 따라서 다리에 있는 트럭을 잘 설계해야 한다.
1초가 지날때마다 대기중인 트럭이 올라갈 수 있는지 판단
"""

def solution(bridge_length, weight, truck_weights):
    arrive_list = []
    bridge = [0] * bridge_length
    trcucks = truck_weights

    print(bridge)

    return 0

if __name__ == '__main__':
    lengths = 2
    weight = 10
    truck_weights = [7,4,5,6]	
    r = solution(bridge_length=lengths, weight=weight, truck_weights=truck_weights)
    print(r)