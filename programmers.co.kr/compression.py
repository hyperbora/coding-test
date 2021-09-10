"""
https://programmers.co.kr/learn/courses/30/lessons/17684
[3차] 압축
"""
from typing import List
import unittest


def solution(msg: str) -> List[int]:
    answer: List[int] = []
    dictionary: List[str] = [chr(i + ord('A') - 1) for i in range(27)]
    length: int = len(msg)
    index: int = 0

    while index < length:
        for i in range(len(dictionary) - 1, -1, -1):
            if msg.startswith(dictionary[i], index):
                answer.append(i)
                found = msg.index(dictionary[i], index)
                if found + len(dictionary[i]) < length:
                    dictionary.append(
                        dictionary[i] + msg[found + len(dictionary[i])])
                index += len(dictionary[i])
                break

    return answer


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertListEqual(solution(msg="KAKAO"),	[11, 1, 27, 15])
        self.assertListEqual(solution(msg="TOBEORNOTTOBEORTOBEORNOT"), [
                             20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34])
        self.assertListEqual(solution(msg="ABABABABABABABAB"), [
                             1, 2, 27, 29, 28, 31, 30])


if __name__ == "__main__":
    unittest.main()
