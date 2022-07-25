from collections import defaultdict
def solution(clothes):
    clothes_dict = defaultdict(int)
    for value, key in clothes:
        clothes_dict[key] += 1
    answer = 1
    for key in clothes_dict.keys():
        answer *= (clothes_dict[key] + 1)
    return answer - 1

clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))