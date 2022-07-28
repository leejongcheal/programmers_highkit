from collections import defaultdict, deque
def bfs(start, n, graph):
    check = [0]*(n+1)
    check[start] = 1
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for next in graph[now]:
            if check[next] == 0:
                check[next] = 1
                q.append(next)
    return check

def solution(n, wires):
    res = 1e19
    graph = defaultdict(list)
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        A = bfs(1, n, graph)
        for i in range(2, n+1):
            if A[i] == 0:
                B = bfs(i, n, graph)
                break
        res = min(res,abs(sum(A) - sum(B)))
        graph[a].append(b)
        graph[b].append(a)
    return res

wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
n = 9
print(solution(n, wires))