"""
https://programmers.co.kr/learn/courses/30/lessons/85002
복서 정렬하기

복서 선수들의 몸무게 weights와, 복서 선수들의 전적을 나타내는 head2head가 매개변수로 주어집니다. 
복서 선수들의 번호를 다음과 같은 순서로 정렬한 후 return 하도록 solution 함수를 완성해주세요.

1. 전체 승률이 높은 복서의 번호가 앞쪽으로 갑니다. 아직 다른 복서랑 붙어본 적이 없는 복서의 승률은 0%로 취급합니다.
2. 승률이 동일한 복서의 번호들 중에서는 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞쪽으로 갑니다.
3. 자신보다 무거운 복서를 이긴 횟수까지 동일한 복서의 번호들 중에서는 자기 몸무게가 무거운 복서의 번호가 앞쪽으로 갑니다.
4. 자기 몸무게까지 동일한 복서의 번호들 중에서는 작은 번호가 앞쪽으로 갑니다.
"""

from typing import List, Tuple
import unittest


def solution(weights, head2head) -> List[int]:
    arr: List[Tuple[float]] = []
    for player_index, (player_weight, play_results) in enumerate(zip(weights, head2head), 1):
        length: int = 0
        win_count: int = 0
        heavy_count: int = 0
        for i, play_result in enumerate(play_results):
            if play_result == "W":
                win_count += 1
                if player_weight < weights[i]:
                    heavy_count += 1
                length += 1
            elif play_result == "L":
                length += 1
        if length == 0:
            length = 1
        arr.append((-win_count / length, -heavy_count, -
                    player_weight, player_index))
        arr.sort()
    return [item[3] for item in arr]


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertListEqual(solution(weights=[50, 82, 75, 120], head2head=[
                             "NLWL", "WNLL", "LWNW", "WWLN"]),	[3, 4, 1, 2])
        self.assertListEqual(solution(weights=[145, 92, 86], head2head=[
                             "NLW", "WNL", "LWN"]),	[2, 3, 1])
        self.assertListEqual(solution(weights=[60, 70, 60], head2head=[
                             "NNN", "NNN", "NNN"]),	[2, 1, 3])


if __name__ == "__main__":
    unittest.main()
