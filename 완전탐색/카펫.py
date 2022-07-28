def solution(brown, yellow):
    answer = []  # m, n 꼴이고 m >= n
    for ym in range(1, yellow+1):
        yn = yellow//ym
        if yn > ym or yn*ym != yellow:
            continue
        now = 0
        bn, bm = yn, ym
        while now < brown:
            bn += 1
            bm += 1
            now += bn * bm - (bn - 1) * (bm - 1)
        if now == brown:
            return [bm, bn]
    return answer


brown = 24
yellow = 24
print(solution(brown, yellow))
