from itertools import product
def solution(numbers, target):
    answer = 0
    r = len(numbers)
    for oper in list(product(["+","-"], repeat = r)):
        now = 0
        for index, op in enumerate(oper):
            if op == "-":
                now -= numbers[index]
            else:
                now += numbers[index]
        if now == target:
            answer += 1
    return answer
numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))