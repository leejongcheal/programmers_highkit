from collections import defaultdict
dir = [(-1, 0),(-1, 1),(0, 1),(1, 1),(1, 0),(1, -1),(0, -1),(-1, -1)]
def solution(arrows):
    answer = 0
    graph = defaultdict(int)
    track = defaultdict(int)
    graph[(0,0)] = 1
    x, y = 0, 0
    for d in arrows:
        dx, dy = dir[d]
        for i in range(2):
            nx, ny = x + dx, y + dy
            if graph[(nx ,ny)] == 1 and track[(x, y, nx, ny)] == 0 and track[(nx, ny,x, y)] == 0:
                answer += 1
            graph[(nx, ny)] = 1
            track[(x, y, nx, ny)] = 1
            x, y = nx, ny
    return answer

arrows = [6, 5, 2, 7, 1, 4, 2, 4, 6]
print(solution(arrows))