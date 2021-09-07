"""
https://programmers.co.kr/learn/courses/30/lessons/17682
[1차] 다트 게임
"""
import unittest


def solution(dartResult: str) -> int:
    nums = [0]

    for s in dartResult:
        if s == 'S':
            nums[-1] **= 1
            nums.append(0)
        elif s == 'D':
            nums[-1] **= 2
            nums.append(0)
        elif s == 'T':
            nums[-1] **= 3
            nums.append(0)
        elif s == '*':
            # 이전 값, 그 이전 값 모두 두 배 처리
            nums[-2] *= 2
            if len(nums) > 2:
                nums[-3] *= 2
        elif s == '#':
            nums[-2] *= -1
        else:
            # 자릿수 올림
            nums[-1] = nums[-1] * 10 + int(s)

    return sum(nums)


"""
1	1S2D*3T     37      11 * 2 + 22 * 2 + 33
2	1D2S#10S	9       12 + 21 * (-1) + 101
3	1D2S0T      3       12 + 21 + 03
4	1S*2T*3S	23      11 * 2 * 2 + 23 * 2 + 31
5	1D#2S*3S	5       12 * (-1) * 2 + 21 * 2 + 31
6	1T2D3D#	    -4      13 + 22 + 32 * (-1)
7	1D2S3T*	    59      12 + 21 * 2 + 33 * 2
"""


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(solution("1S2D*3T"), 37)
        self.assertEqual(solution("1D2S#10S"), 9)
        self.assertEqual(solution("1D2S0T"), 3)
        self.assertEqual(solution("1S*2T*3S"), 23)
        self.assertEqual(solution("1D#2S*3S"), 5)
        self.assertEqual(solution("1T2D3D#"), -4)
        self.assertEqual(solution("1D2S3T*"), 59)


if __name__ == "__main__":
    unittest.main()
