"""
0-1 배낭 문제(0-1 knapsack problem)
다이나믹 프로그래밍으로 풀 수 있으며 모든 경우의 수를 계산해야 한다.
"""
from typing import List, Tuple
import unittest


def zero_one_knapsack(cargo: List[Tuple], capacity: int) -> int:
    """
    cargo : 배낭 리스트 각 각의 아이템의 (돈, 무게)를 나타낸다.
    pack : 리스트 변수에 2차원 행렬 데이터를 저장한다.
            행 사이즈 : len(cargo) + 1
            열 사이즈 : capacity + 1
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 6, 6, 6],
        [0, 2, 2, 2, 10, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
        [0, 2, 3, 3, 10, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],
        [0, 2, 3, 4, 10, 12, 13, 14, 15, 15, 15, 15, 15, 15, 15, 15]
    ]
    """
    pack: List[List[int]] = []

    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i - 1][1] <= c:
                # 현재 아이템이 배낭의 무게를 넘지 않을 때
                # 배낭에 현재 아이템을 추가해서 얻는 돈과 다이나믹 프로그래밍으로 미리 계산한
                # 현재 수용가능한 무게에서 현재 아이템 무게를 뺀만큼의 공간에서 얻는 돈을 더한 값과
                # 현재 아이템을 추가하지 않을 때 얻을 수 있는 돈을 비교해서
                # 최대값을 저장한다.
                pack[i].append(
                    max(cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                        pack[i - 1][c])
                )
            else:
                # 현재 아이템의 무게가 배낭 무게를 초과하므로
                # 이전 데이터를 그대로 저장한다.
                pack[i].append(pack[i - 1][c])

    # 마지막 데이터를 리턴한다.
    return pack[-1][-1]


class TestSolution(unittest.TestCase):
    def test_result(self):
        cargo = [
            (4, 12),
            (2, 1),
            (10, 4),
            (1, 1),
            (2, 2)
        ]
        self.assertEqual(zero_one_knapsack(cargo, 15), 15)


if __name__ == "__main__":
    unittest.main()
