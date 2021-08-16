"""
https://programmers.co.kr/learn/courses/30/lessons/17677
[1차] 뉴스 클러스터링
"""
from collections import Counter


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    cnt_1 = Counter([str1[i:i+2]
                    for i in range(0, len(str1) - 1) if str1[i:i+2].isalpha()])
    cnt_2 = Counter([str2[i:i+2]
                    for i in range(0, len(str2) - 1) if str2[i:i+2].isalpha()])
    intersection = []
    union = []
    for key in cnt_1:
        if key in cnt_2:
            intersection.extend([key] * min(cnt_1[key], cnt_2[key]))
            union.extend([key] * max(cnt_1[key], cnt_2[key]))
        else:
            union.extend([key] * cnt_1[key])
    for key in cnt_2:
        if key not in cnt_1:
            union.extend([key] * cnt_2[key])
    result = 0
    if len(intersection) == 0 and len(union) == 0:
        result = 1
    else:
        result = len(intersection) / len(union)
    return int(result * 65536)


"""
str1	str2	answer
FRANCE	french	16384
handshake	shake hands	65536
aa1+aa2	AAAA12	43690
E=M*C^2	e=m*c^2	65536
"""

if __name__ == "__main__":
    str1 = "FRANCE"
    str2 = "french"
    print(solution(str1, str2))
    str1 = "handshake"
    str2 = "shake hands"
    print(solution(str1, str2))
    str1 = "aa1+aa2"
    str2 = "AAAA12"
    print(solution(str1, str2))
    str1 = "E=M*C^2"
    str2 = "e=m*c^2"
    print(solution(str1, str2))
