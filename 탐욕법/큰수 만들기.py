def solution(number, k):
    stack = []
    number = list(number[::-1])
    while number:
        if not stack:
            stack.append(number.pop())
            continue
        while stack and number[-1] > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(number.pop())
    for i in range(k):
        stack.pop()
    return "".join(stack)


number = "4177255555"
k = 4
print(solution(number, k))