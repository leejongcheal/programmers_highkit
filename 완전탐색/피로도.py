from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for comb in permutations([i for i in range(len(dungeons))],len(dungeons) ):
        now = k
        cnt = 0
        for i in comb:
            a, b = dungeons[i]
            if now >= a:
                cnt += 1
                now -= b
            else:
                break
        answer = max(answer, cnt)
    return answer


dungeons = 	[[80,20],[50,40],[30,10]]
k = 80
print(solution(k, dungeons))