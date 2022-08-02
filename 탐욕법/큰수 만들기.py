def solution(number, k):
    answer = []
    number = list(number)
    index = 0
    while k != 0 and len(number) > k:
        next_index = number[:k + 1].index(max(number[:k + 1]))
        k -= next_index
        answer.append(number[next_index])
        number = number[next_index+1:]
    if k == 0:
        for i in number:
            answer.append(i)
    return "".join(answer)

number = "4177255555"
k = 4
print(solution(number, k))