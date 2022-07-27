def solution(s):
    answer = True
    q = []
    for ss in s:
        if ss == "(":
            q.append(ss)
        else:
            if not q:
                return False
            else:
                q.pop()
    if q:
        return False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return True

s = "()()"
print(solution(s))