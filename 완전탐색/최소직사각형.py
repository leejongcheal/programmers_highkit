def solution(sizes):
    sizes.sort()
    max_col = sizes[-1][0]
    sizes.sort(key=lambda x:x[1])
    max_col = max(max_col, sizes[-1][1])
    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            sizes[i] = [sizes[i][1], sizes[i][0]]
    sizes.sort(key=lambda x:x[1])
    row = sizes[-1][1]
    return row * max_col
    # return max([max(x) for x in sizes]) * max([min(x) for x in sizes])
    # 이런식으로 멋지게 한줄풀이가 가능함 -> 알고리즘은 맞았네 그래도
sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))














