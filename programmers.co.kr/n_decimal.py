"""
https://programmers.co.kr/learn/courses/30/lessons/17687
[3차] n진수 게임
"""

from typing import List
import unittest


def solution(n: int, t: int, m: int, p: int) -> str:
    def get_num(num: int):
        return num if num < 10 else chr(ord('A') + num - 10)

    def transform(num: int) -> str:
        arr: List[str] = []
        d: int = num
        while True:
            d, m = divmod(d, n)
            arr.append(str(get_num(m)))
            if d < n:
                if d != 0:
                    arr.append(str(get_num(d)))
                break
        return ''.join(reversed(arr))
    answer: List[str] = []
    num: int = 0
    index: int = 0
    while t > 0:
        new_num: str = transform(num)
        for i in range(len(new_num)):
            if index % m == p - 1 and t > 0:
                answer.append(new_num[i])
                t -= 1
            index += 1
        num += 1
    return ''.join(answer)


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(solution(n=2, t=4, m=2, p=1), "0111")
        self.assertEqual(solution(n=16, t=16, m=2, p=1), "02468ACE11111111")
        self.assertEqual(solution(n=16, t=16, m=2, p=2), "13579BDF01234567")


if __name__ == "__main__":
    unittest.main()
