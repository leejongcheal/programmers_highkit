from collections import defaultdict
def solution(participant, completion):
    dict  = defaultdict(int)
    for key in participant:
        dict[key] += 1
    for key in completion:
        dict[key] -= 1
    for key in participant:
        if dict[key] != 0:
            return key



participant = ["mislav", "stanko", "mislav", "ana"]
completion =  ["stanko", "ana", "mislav"]
a = solution(participant, completion)
print(a)