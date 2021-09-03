"""
https://leetcode.com/problems/different-ways-to-add-parentheses/
숫자와 연산자를 입력받아 괄호를 추가하여 가능한 모든 조합의 결과를 출력
"""
from typing import List
import unittest


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        """
        *, -, + 연산자가 등장할 때 좌/우 분할을 하고 각각 계산 결과를 리턴한다.
        연산자를 기준으로 재귀로 left, right를 계속 분할하고 분할된 값은
        compute() 함수로 계산할 결과를 extend()로 확장한다.
        분할 결과를 리턴받으려면 input이 숫자형일 때 리턴하게 한다.
        이렇게 하면 분할의 결과가 최종적으로 숫자형인 타입을 재귀의 최종 결과로 리턴하게 된다.

        마지막 계산 직전에는 right는 리스트가 된다. 각각 반복으로 단수형 값을 추출해 계산한다.
        eval() 함수는 문자열을 파싱하고 파이썬 표현식으로 처리해주는 역할을 한다.
        """
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        if input.isdigit():
            return [int(input)]

        results = []
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysToCompute(input=input[:index])
                right = self.diffWaysToCompute(input=input[index + 1:])

                results.extend(compute(left=left, right=right, op=value))
        return results


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertCountEqual(s.diffWaysToCompute(input="2-1-1"), [0, 2])
        self.assertCountEqual(s.diffWaysToCompute(
            input="2*3-4*5"), [-34, -14, -10, -10, 10])


if __name__ == "__main__":
    unittest.main()
