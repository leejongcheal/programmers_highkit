import math
def solution(progresses, speeds):
    answer = []
    now = 0
    answer_i = -1
    i = 0
    while i < len(speeds):
        if now*speeds[i] + progresses[i] >= 100:
            answer[answer_i] += 1
        else:
            answer.append(1)
            answer_i += 1
            now = math.ceil((100 - progresses[i]) / speeds[i])
            # if now*10 != int(now*10):
            #     now = int(now) + 1
            # else:
            #     now = int(now)
        i += 1
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = 	[1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))