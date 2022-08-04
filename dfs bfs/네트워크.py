def find_parent(a, parent):
    if a == parent[a]:
        return a
    parent[a] = find_parent(parent[a], parent)
    return parent[a]
def union(a, b, parent):
    A, B = find_parent(a, parent), find_parent(b, parent)
    if A > B:
        parent[B] = parent[A]
    else:
        parent[A] = parent[B]
def solution(n, computers):
    answer = set()
    parent = [i for i in range(n)]
    for index, list in enumerate(computers):
        for next, val in enumerate(list):
            if val and find_parent(index, parent) != find_parent(next, parent):
                union(index, next, parent)
    for i in range(n):
        answer.add(find_parent(i, parent))
    return len(answer)

n = 3
computers = 	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))