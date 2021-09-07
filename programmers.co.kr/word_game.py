"""
https://programmers.co.kr/learn/courses/30/lessons/12981
영어 끝말잇기
"""
from typing import List, Set
import unittest
import math


def solution(n, words) -> List[int]:
    answer: List[int] = []

    s: Set = set()
    prev: str = ""
    for i, word in enumerate(words, 1):
        if word not in s and (not prev or prev[-1] == word[0]):
            s.add(word)
        else:
            d: int = math.ceil(i / n)
            m: int = i % n
            if m == 0:
                m = n
            answer.extend([m, d])
            break
        prev = word
    if not answer:
        answer.extend([0, 0])
    return answer


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertListEqual(solution(n=3, words=[
                             "tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]), [3, 3])
        self.assertListEqual(solution(n=5, words=["hello", "observe", "effect", "take", "either", "recognize", "encourage",
                                                  "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]), [0, 0])
        self.assertListEqual(solution(
            n=2, words=["hello", "one", "even", "never", "now", "world", "draw"]), [1, 3])


if __name__ == "__main__":
    unittest.main()
