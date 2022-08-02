def updown(char):
    if ord(char) - ord("A") > ord("Z") - ord(char) + 1:
        return ord("Z") - ord(char) + 1
    else:
        return ord(char) - ord("A")
def direction(index, name, dir, check):
    i = 1
    dir_cnt = 1
    while check[(index + dir*i) % len(name)] == 1:
        dir_cnt += 1
        i += 1
    redir_cnt = 1
    i = 1
    while check[(index - (dir*i)) % len(name)] == 1:
        redir_cnt += 1
        i += 1
    if redir_cnt > dir_cnt:
        return dir_cnt, dir
    else:
        return redir_cnt, -dir
def solution(name):
    if name == "A"*len(name):
        return 0
    answer = 0
    index = 0
    check = [0]*len(name)
    name_cnt = [0]*len(name)
    for i in range(len(name)):
        if name[i] == "A":
            check[i] = 1
        name_cnt[i] = updown(name[i])
    index = 0
    dir = 1
    while 1:
        answer += name_cnt[index]
        check[index] = 1
        if sum(check) == len(name):
            break
        # 방향 고르기
        move, dir = direction(index, name, dir, check)
        answer += move
        index = (index + move * dir) % len(name)
    return answer

name = "BBBBAAAABA"
print(solution(name))