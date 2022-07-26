def minus_index(now_truck, resume_dist, index):
    new_dist = []
    new_truck = []
    for i in range(len(now_truck)):
        if resume_dist[i] - index != 0:
            new_dist.append(resume_dist[i] - index)
            new_truck.append(now_truck[i])
    return new_truck, new_dist
def solution(bridge_length, weight, truck_weights):
    next_truck = 0
    now_truck = []
    resume_dist = []
    time = 1
    while 1:
        flag = 0
        # 트럭올릴수 있는경우 확인
        if len(now_truck) < bridge_length and sum(now_truck) < weight:
            # 올릴 트럭이 없는경우이 없고 다 도착한경우
            if next_truck == len(truck_weights):
                if len(now_truck) == 0:
                    return time
            # 올릴 트럭이 있는 경우
            else:
                # 트럭을 올릴수 있는경우
                if sum(now_truck) + truck_weights[next_truck] <= weight:
                    now_truck.append(truck_weights[next_truck])
                    next_truck += 1
                    resume_dist.append(bridge_length)
                    now_truck, resume_dist = minus_index(now_truck, resume_dist, 1)
                    time += 1
                    flag = 1
        # 이미 올라간 상태에서 시간을 효율적 계산하기
        if now_truck and flag == 0:
            time += resume_dist[0]
            now_truck, resume_dist = minus_index(now_truck, resume_dist,resume_dist[0])

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(1)
print(solution(bridge_length, weight, truck_weights), 555)

# https://school.programmers.co.kr/learn/courses/30/lessons/42583