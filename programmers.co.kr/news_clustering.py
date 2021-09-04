"""
https://programmers.co.kr/learn/courses/30/lessons/17677
[1차] 뉴스 클러스터링
"""
from collections import Counter
import collections
import unittest
import re


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


def solution2(str1, str2):
    # 두 글자씩 끊어서 다중집합 구성
    str1s = [
        str1[i:i + 2].lower()
        for i in range(len(str1) - 1)
        if re.findall('[a-z]{2}', str1[i:i + 2].lower())
    ]
    str2s = [
        str2[i:i + 2].lower()
        for i in range(len(str2) - 1)
        if re.findall('[a-z]{2}', str2[i:i + 2].lower())
    ]

    # 교집합 계산
    intersection = sum((collections.Counter(str1s) &
                        collections.Counter(str2s)).values())
    # 합집합 계산
    union = sum((collections.Counter(str1s) |
                 collections.Counter(str2s)).values())

    # 자카드 유사도 계산
    jaccard_sim = 1 if union == 0 else intersection / union
    return int(jaccard_sim * 65536)


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(solution("FRANCE", "french"), 16384)
        self.assertEqual(solution("handshake", "shake hands"), 65536)
        self.assertEqual(solution("aa1+aa2", "AAAA12"), 43690)
        self.assertEqual(solution("E=M*C^2", "e=m*c^2"), 65536)

        self.assertEqual(solution2("FRANCE", "french"), 16384)
        self.assertEqual(solution2("handshake", "shake hands"), 65536)
        self.assertEqual(solution2("aa1+aa2", "AAAA12"), 43690)
        self.assertEqual(solution2("E=M*C^2", "e=m*c^2"), 65536)


if __name__ == "__main__":
    unittest.main()
