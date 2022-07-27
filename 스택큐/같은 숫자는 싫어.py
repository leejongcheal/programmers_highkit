def solution(arr):
    if not arr:
        return []
    answer = [arr[0]]
    for a in arr:
        if a != answer[-1]:
            answer.append(a)
    return answer

# arr = [1,1,3,3,0,1,1]
arr = []
print(solution(arr))