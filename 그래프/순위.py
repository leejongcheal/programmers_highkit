def solution(n, results):
    answer = 0
    INF = int(1e10)
    graph = [[INF]*n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for a, b in results:
        graph[b-1][a-1] = 1
    for a in range(n):
        for b in range(n):
            for k in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    for i in range(n):
        flag = 0
        for j in range(n):
            if graph[i][j] == INF and graph[j][i] == INF:
                flag = 1
                break
        if flag:
            continue
        answer += 1
    return answer

results = 	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
n = 5
print(solution(n, results))