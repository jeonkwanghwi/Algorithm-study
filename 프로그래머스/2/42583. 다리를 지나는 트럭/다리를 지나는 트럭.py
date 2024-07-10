
from collections import deque
def solution(bridge_length, weight, truck_weights):

    truck_weights = deque(truck_weights)  # truck_weights를 deque로 변환
    onthebridge = deque([0] * bridge_length)
    time = 0
    current_bridge_weight = 0

    while onthebridge:
        time += 1
        # 다리에서 트럭 한 대가 내려감
        current_bridge_weight -= onthebridge.popleft()

        if truck_weights:
            # 다음 트럭이 다리에 올라갈 수 있는지 확인
            if current_bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                onthebridge.append(truck)
                current_bridge_weight += truck
            else:
                onthebridge.append(0)

        # 모든 트럭이 다리를 건넜으면 반복을 종료
        if not onthebridge and not truck_weights:
            break

    return time