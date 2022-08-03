def find_parent(a, parent):
    if a == parent[a]:
        return a
    else:
        parent[a] = find_parent(parent[a], parent)
        return parent[a]
def union(a, b, parent):
    A, B = find_parent(a, parent), find_parent(b, parent)
    if A <= B:
        parent[B] = A
    else:
        parent[A] = B
def solution(n, costs):
    INF = 1e10
    answer = 0
    costs.sort(key=lambda x:x[2])
    parent = [i for i in range(n)]
    for a, b, c in costs:
        if find_parent(a, parent) != find_parent(b, parent):
            union(a, b, parent)
            answer += c
    return answer
n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))