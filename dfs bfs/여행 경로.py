from collections import defaultdict

def dfs(now, check, graph):
    global answer, n
    if len(answer) == n:
        return 1
    for next in graph[now]:
        if check[(now, next)] != 0:
            check[(now, next)] -= 1
            answer.append(next)
            if dfs(next, check, graph):
                return 1
            check[(now, next)] += 1
            answer.pop()
    return 0


def solution(tickets):
    start = "ICN"
    graph = defaultdict(list)
    check = defaultdict(int)
    for a, b in tickets:
        graph[a].append(b)
        check[(a, b)] += 1
    for key in graph.keys():
        graph[key].sort()
    global answer, n
    n = len(tickets) + 1
    answer = [start]
    dfs(start, check, graph)

    return answer

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))

print(
    solution(
        [["ICN", "B"], ["B", "C"], ["C", "ICN"], ["ICN", "D"], ["ICN", "E"], ["E", "F"]]
    )
    == ["ICN", "B", "C", "ICN", "E", "F", "D"]
)