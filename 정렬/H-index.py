from bisect import bisect_left
def solution(citations):
    res = 0
    citations.sort()
    prev = -1
    prev_cnt = 0
    for i in range(len(citations)):
        if citations[i] != prev:
            now = citations[i]
            cnt = len(citations) - i
            if cnt >= now and prev_cnt <= now:
                res = citations[i]
            prev = now
            prev_cnt = len(citations) - cnt
    return res

citations = [2,2,3,3,4,4]
print(solution(citations))