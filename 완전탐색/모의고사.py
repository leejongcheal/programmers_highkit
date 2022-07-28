def solution(answers):
    answer = []
    people = [[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4,5, 5]]
    res = [0, 0, 0]
    for i in range(len(answers)):
        for p in range(3):
            if people[p][i%len(people[p])] == answers[i]:
                res[p] += 1
    max_r = max(res)
    for i in range(3):
        if res[i] == max_r:
            answer.append(i+1)
    return answer


answers = [1,3,2,4,2]
print(solution(answers))