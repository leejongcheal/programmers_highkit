# from bisect import bisect_right
from collections import deque
def solution(people, limit):
    people.sort()
    answer = 0
    people = deque(sorted(people))
    while people:
        now = people.pop()
        if people and now + people[0] <= limit:
            people.popleft()
        answer += 1
    return answer

    # 이진탐색 풀이 삭제부분에서 시간초과 뜸 -> 이를 해결하는것도 공부하기
    # 그냥 맨앞과 맨뒤만 비교하면 되는 문제였네 ... 해결방법도 공부는 하자 일단.
    # 굳이 활용하는방법은 bisect_lfet(a,x, l0, hi) lo와 hi를 활용하는건데 이런경우엔 실효성 떨어짐
    # 즉, 이런경우엔 어쩔수없음을 이해하고 기억하자
    # while people:
    #     now = people.pop()
    #     pair_value = limit - now
    #     index = bisect_right(people, pair_value)
    #     if index != 0:
    #         del people[index - 1]
    #     answer += 1
    # return answer

people = [40,50,150,160]
limit = 200
print(solution(people, limit))