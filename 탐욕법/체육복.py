from collections import defaultdict
def solution(n, lost, reserve):
    answer = n
    reserve = set(reserve)
    new_lost = []
    for l in lost:
        if l not in reserve:
            answer -= 1
            new_lost.append(l)
        else:
            reserve.remove(l)
    lost = new_lost
    lost.sort()
    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
            answer += 1
        elif l+1 in reserve:
            reserve.remove(l + 1)
            answer += 1
    return answer
n= 10
lost= [8, 10]
reserve= [6,7,9]
print(solution(n, lost, reserve))