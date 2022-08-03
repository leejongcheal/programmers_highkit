def solution(routes):
    routes.sort(key=lambda x: x[1])
    check = [0]*len(routes)
    index = 0
    answer = 0
    while sum(check) != len(check):
        now = routes[index][1]
        # print(now)
        check[index] = 1
        answer += 1
        while 1 and index + 1 < len(routes):
            index += 1
            if routes[index][0] <= now <= routes[index][1]:
                check[index] = 1
            else:
                break

    return answer


routes = [[-100,100],[50,170],[150,200],[-50,-10],[10,20],[30,40]]
print(solution(routes))