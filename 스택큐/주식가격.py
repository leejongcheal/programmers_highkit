def solution(prices):
    answer = [0]*len(prices)
    stack = []
    for i in range(len(prices)):
        if not stack:
            stack.append(i)
        else:
            while stack and prices[stack[-1]] > prices[i]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
    while stack:
        j = stack.pop()
        answer[j] = i - j
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))