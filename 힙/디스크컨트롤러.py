import heapq
def solution(jobs):
    cnt = len(jobs)
    jobs.sort(reverse=True)
    answer = 0
    hard = []
    scheduler = []
    now_time = 0
    now_job = 0
    while jobs:
        # 처음 작업 넣기
        if jobs:
            now_job = jobs.pop()
            now_time = now_job[0] + now_job[1]
            answer += now_job[1]
        while now_job != 0:
            while jobs and now_time >= jobs[-1][0]:
                a, b = jobs.pop()
                heapq.heappush(scheduler, [b, a])
            now_job = 0
            if scheduler:
                b, a = heapq.heappop(scheduler)
                now_time += b
                now_job = [a, b]
                answer += (now_time - a)
    return answer // cnt


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))

# https://school.programmers.co.kr/learn/courses/30/lessons/42627