import heapq
def solution(operations):
    q = []
    for op in operations:
        a, b = op.split()
        b = int(b)
        if a == "I":
            heapq.heappush(q, b)
        elif q:
            if b > 0:
                q = heapq.nlargest(len(q), q)[1:]
                heapq.heapify(q)
            else:
                heapq.heappop(q)
    if q:
        return [heapq.nlargest(1, q)[0], q[0]]
    else:
        return [0, 0]

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))