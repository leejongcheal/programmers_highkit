from bisect import bisect_left
def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    n = len(citations)
    for i in range(n):
        if i+1 <= citations[i]:
            answer = i+1
    return answer

citations = [3, 0, 6, 1, 5]
print(solution(citations))