from collections import defaultdict
def solution(phone_book):
    len_dict = set()
    for phone in phone_book:
        len_dict.add(len(phone))
    len_dict = list(len_dict)
    prefix = defaultdict(int)
    for phone in phone_book:
        now_len = len(phone)
        for length in len_dict:
            if length <= now_len:
                prefix[phone[:length]] += 1
    for phone in phone_book:
        if prefix[phone] > 1:
            return False
    return True

phone_book = ["123","456","789"]
print(solution(phone_book))

# https://school.programmers.co.kr/learn/courses/30/lessons/42577