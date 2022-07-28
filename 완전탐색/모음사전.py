def solution(word):
    word = list(word)
    order = ['A', 'E', 'I', 'O', 'U']
    wci = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    index = 1
    now = ["A"]
    while now != word:
        index += 1
        if len(now) != 5:
            now.append(order[0])
        else:
            while now:
                i = wci[now[-1]]
                if i + 1 == 5:
                    now.pop()
                else:
                    now[-1] = order[i+1]
                    break
    return index


word = "I"
print(solution(word))