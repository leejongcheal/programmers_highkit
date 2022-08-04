from collections import deque

def solution(rectangle, characterX, characterY, ey, ex):
    n = 101
    graph = [[0]*n for i in range(n)]
    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        # 가장 자리값 1로 넣어주기
        if graph[y1][x1] == 0 or graph[y1][x1] == 1:
            graph[y1][x1] = 1
        x, y = x1, y1
        for dy, dx in dir:
            while 1:
                nx, ny = x + dx, y + dy
                if (y1, x1) <= (ny, nx) <= (y2, x2):
                    if graph[ny][nx] == 0 or graph[ny][nx] == 1:
                        graph[ny][nx] = 1
                    x, y = nx, ny
                else:
                    break
        # 가장자리 제외 2로 넣어주기
        for i in range(y1 + 1, y2):
            for j in range(x1 + 1, x2):
                graph[i][j] = 2
    # 이제 값 구하기
    x, y = characterY*2, characterX*2
    ex *= 2
    ey *= 2
    graph[x][y] = 2
    q = deque()
    q.append((x, y, 0))
    while q:
        x, y, cost = q.popleft()
        if x == ex and y == ey:
            return cost // 2
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 2
                q.append((nx, ny ,cost + 1))

# 이건 진짜 시간이너무 오래걸리는 문제
# 빠른시간내에 풀기에는 배열문제 + *2해서 풀어야하는 문제
# 즉, 어떻게 표현할것인지 -> 예외상황 안생기는지 파악할줄 알아야 하는문제
# 그냥 1~7에 1값넣어줘서 풀려니깐
# 1222
# 1122  처럼 ㄷ 에서 1 사각형이 나올수도 있음....
# 1122
# 1222
print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))
