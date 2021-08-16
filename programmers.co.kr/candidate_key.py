"""
https://programmers.co.kr/learn/courses/30/lessons/42890
후보키
"""
from itertools import combinations


def solution(relation):
    answer = 0
    rows = len(relation)
    cols = len(relation[0])
    key_list = []
    for i in range(1, cols + 1):
        answer += sum([candidate_key_validation(relation, c, rows, key_list)
                      for c in combinations(range(cols), i)])
    return answer


def candidate_key_validation(relation, indexes, rows, key_list):
    for key in key_list:
        count = 0
        for index in indexes:
            if index in key:
                count += 1
        if count == len(key):
            return 0
    s = set()
    for r in relation:
        lst = []
        for i in indexes:
            lst.append(r[i])
        s.add("".join(lst))
    if len(s) == rows:
        key_list.append(indexes)
        return 1
    return 0


if __name__ == "__main__":
    relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
        "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
    print(solution(relation))
