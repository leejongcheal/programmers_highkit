def solution(priorities, location):
    answer = 0
    order = sorted(priorities)
    cnt = 0
    while len(order):
        if priorities[0] == order[-1]:
            cnt += 1
            if location == 0:
                return cnt
            location -= 1
            priorities = priorities[1:]
            order.pop()
        else:
            priorities = priorities[1:] + [priorities[0]]
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))