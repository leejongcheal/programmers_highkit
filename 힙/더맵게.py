import heapq
def solution(scoville, K):
    answer = 0
    q = []
    for s in scoville:
        heapq.heappush(q, s)
    while len(q) >= 2:
        if q[0] >= K:
            return answer
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        heapq.heappush(q, a+2*b)
        answer += 1
    if q[0] >= K:
        return answer
    return -1

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))