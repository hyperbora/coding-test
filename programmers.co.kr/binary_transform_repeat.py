from typing import List
import unittest


def solution(s) -> List[int]:
    count: int = 0
    acc_zero_count: int = 0
    while s != "1":
        zero_count = s.count('0')
        s = bin(len(s) - zero_count)[2:]
        count += 1
        acc_zero_count += zero_count
    return [count, acc_zero_count]


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertListEqual(solution(s="110010101001"), [3, 8])
        self.assertListEqual(solution(s="01110"),	[3, 3])
        self.assertListEqual(solution(s="1111111"),	[4, 1])


if __name__ == "__main__":
    unittest.main()
