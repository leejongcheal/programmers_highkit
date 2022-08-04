import heapq
from collections import defaultdict
def solution(begin, target, words):
    if target not in words:
        return 0
    # 0이면 가장큰값으로 예외처리
    res = defaultdict(int)
    graph = defaultdict(list)
    for now in [begin] + words:
        for next in words:
            cnt = 0
            for i in range(len(now)):
                if now[i] != next[i]:
                    cnt += 1
            if cnt == 1:
                graph[now].append(next)
    q = []
    for next in graph[begin]:
        res[next] = 1
        heapq.heappush(q,(1, next))
    while q:
        now_cost, now = heapq.heappop(q)
        if res[now] < now_cost:
            continue
        for next in graph[now]:
            if res[next] == 0 or now_cost + 1 < res[next]:
                res[next] = now_cost + 1
                heapq.heappush(q,(now_cost + 1, next))
    return res[target]


begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]
# print(solution(begin, target, words))
# print(solution("hit", "wow", ["hot", "dog", "dot", "wow"]))
#
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]))
print(solution("1234567000", "1234567899", [
      "1234567800", "1234567890", "1234567899"]))
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]))