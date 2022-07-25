from collections import defaultdict


def solution(genres, plays):
    total = defaultdict(int)
    genre_index = defaultdict(list)
    for i in range(len(genres)):
        total[genres[i]] += plays[i]
        genre_index[genres[i]].append([i, plays[i]])
    answer = []
    genres_list = []
    sort_d = sorted(total.items(), key=lambda x: -x[1])
    for genre, cnt in sort_d:
        now = sorted(genre_index[genre], key=lambda x: -x[1])
        answer.append(now[0][0])
        if len(now) == 1:
            continue
        answer.append(now[1][0])
    return answer


# genres = ["classic", "pop", "classic", "classic", "pop"]
genres = ["a", "a", "a"]
plays = [200, 100, 100]
print(solution(genres, plays))
# https://school.programmers.co.kr/learn/courses/30/lessons/42579