from collections import defaultdict
import math
from itertools import permutations
def Eratosthenes(prime, MAX_NUM):
    prime[0] = 1
    prime[1] = 1
    for i in range(2,int(math.sqrt(MAX_NUM))+1):
        if prime[i] == 0:
            now = i
            j = 2
            while now*j < MAX_NUM:
                prime[now*j] = 1
                j += 1
    return prime


def prime_check(num):
    if num == 0 or num == 1:
        return 0
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return 0
    return 1


def solution(numbers):
    numbers = list(numbers)
    answer = 0
    cand = set()
    for i in range(1, len(numbers)+1):
        for per in permutations(numbers, i):
            now = int("".join(per))
            cand.add(now)
    for can in cand:
        if prime_check(can):
            answer += 1
    return answer


numbers = "011"
print(solution(numbers))