def solution(numbers):
    numbers.sort(key=lambda x:str(x)*3)
    return str(int("".join(map(str,numbers[::-1]))))


numbers = [0, 0, 0, 0]
print(solution(numbers))

# https://school.programmers.co.kr/learn/courses/30/lessons/42746