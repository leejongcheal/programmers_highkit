from collections import defaultdict
def solution(n, lost, reserve):
    answer = n
    reserve = set(reserve)
    new_lost = []
    for l in lost:
        if l not in reserve:
            answer -= 1
            new_lost.append(l)
        else:
            reserve.remove(l)
    lost = new_lost
    flag_while = 1
    while flag_while:
        flag_while = 0
        dict = defaultdict(list)
        for l in lost:
            if l-1 in reserve:
                dict[l].append(l - 1)
            if l+1 in reserve:
                dict[l].append(l + 1)
        new_key = []
        flag1 = 0
        for key in sorted(dict.keys()):
            flag_addkey = 0
            if len(dict[key]) == 1 and dict[key][0] in reserve:
                answer += 1
                flag_addkey = 1
                flag1 = 1
                flag_while = 1
                reserve.remove(dict[key][0])
            elif len(dict[key]) == 2:
                cnt = 0
                for v in dict[key]:
                    if v in reserve:
                        cnt += 1
                if cnt == 1:
                    answer += 1
                    flag_addkey = 1
                    flag1 = 1
                    flag_while = 1
                    for v in dict[key]:
                        if v in reserve:
                            reserve.remove(v)
            if not flag_addkey:
                new_key.append(key)
        lost = new_key
        new_key = []
        # 2개 짜리정리후 lost에 잘넣어서 넘기기
        if not flag1:
            for key in lost:
                v_list = []
                for v in dict[key]:
                    if v in reserve:
                        v_list.append(v)
                if len(v_list) != 0:
                    reserve.remove(v_list[0])
                    answer += 1
                    flag_addkey = 1
                else:
                    new_key.append(key)
            lost = new_key
    return answer

n= 10
lost= [8, 10]
reserve= [6,7,9]
print(solution(n, lost, reserve))