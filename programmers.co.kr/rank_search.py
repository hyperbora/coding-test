"""
https://programmers.co.kr/learn/courses/30/lessons/72412
순위 검색
"""
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []
    d = defaultdict(list)
    all_point = []
    for row in info:
        temp = row.split()
        key = ''.join(temp[:len(temp) - 1])
        point = int(temp[-1])
        all_point.append(point)
        d[key].append(point)
    all_point.sort()
    all_point_length = len(all_point)
    for key in d:
        d[key].sort()
    for q in query:
        conditions = [item for item in q.split() if item != 'and']
        point = int(conditions[-1])
        if conditions.count('-') == 4:
            index = bisect_left(all_point, point)
            if index != all_point_length:
                answer.append(all_point_length - index)
            else:
                answer.append(0)
        else:
            point = int(conditions.pop())
            count = 0
            for key in d:
                for condition in conditions:
                    if condition != '-' and not condition in key:
                        break
                else:
                    index = bisect_left(d[key], point)
                    length = len(d[key])
                    if index != length:
                        count += (length - index)
            answer.append(count)
    return answer


if __name__ == "__main__":
    info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
            "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
    print(solution(info, query))
