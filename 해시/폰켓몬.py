def solution(nums):
    answer = 0
    cnt = len(nums) // 2
    nums = set(nums)
    total = len(nums)
    if total > cnt:
        answer = cnt
    else:
        answer = total
    return answer


# https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3