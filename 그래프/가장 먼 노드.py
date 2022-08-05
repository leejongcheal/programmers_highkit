import heapq
from collections import defaultdict
def solution(n, edge):
    answer = 0
    INF = int(1e10)
    res = [INF]*(n+1)
    res[0] = res[1] = 0
    grapg = defaultdict(list)
    for a, b in edge:
        grapg[a].append(b)
        grapg[b].append(a)
    q = [(0, 1)]
    while q:
        now_cost, now = heapq.heappop(q)
        if now_cost > res[now]:
            continue
        for next in grapg[now]:
            if res[next] > now_cost + 1:
                res[next] = now_cost + 1
                heapq.heappush(q,(res[next], next))
    max_value = max(res)
    answer = res.count(max_value)
    return answer

n = 6
edge = 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4],[5, 2]]
print(solution(n, edge))