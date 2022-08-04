from collections import deque

def solution(maps):
    INF = 1e10
    n, m = len(maps), len(maps[0])
    dir = [(1, 0),(-1, 0),(0, 1),(0, -1)]
    q = deque()
    q.append((0,0))
    while q:
        x, y, c = q.popleft()
        if x == n - 1 and y == m - 1:
            return maps[x][y]
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                q.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
    return -1


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))