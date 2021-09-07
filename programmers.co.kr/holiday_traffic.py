"""
https://programmers.co.kr/learn/courses/30/lessons/17676
[1차] 추석 트래픽
"""
import datetime
import unittest


def solution(lines: str) -> int:
    """
    요청량이 변하는 순간은 각 로그의 시작과 끝뿐임을 알 수 있다.
    """
    # 로그의 시작, 종료 시각 저장
    # 시작은 1, 종료는 -1로 저장
    combined_logs = []
    for log in lines:
        logs = log.split(' ')
        timestamp = datetime.datetime.strptime(
            logs[0] + ' ' + logs[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        combined_logs.append((timestamp, -1))
        combined_logs.append((timestamp - float(logs[2][:-1]) + 0.001, 1))

    # 아직 종료되지 않은 누적된 요청 수 accumulated와
    # 1초 미만 윈도우 범위 내의 모든 요청 수를 합한 값 중에서 최대값을 결과로 갖는다.
    # 매번 1초 미만 윈도우를 계산하는 형태로 구현
    accumulated = 0
    max_requests = 1
    combined_logs.sort(key=lambda x: x[0])
    for i, elem1 in enumerate(combined_logs):
        current = accumulated

        # 1초 미만 윈도우 범위 요청 수 계산
        for elem2 in combined_logs[i:]:
            if elem2[0] - elem1[0] > 0.999:
                break
            if elem2[1] > 0:
                current += elem2[1]
        max_requests = max(max_requests, current)
        accumulated += elem1[1]

    return max_requests


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(solution(lines=[
            "2016-09-15 01:00:04.001 2.0s",
            "2016-09-15 01:00:07.000 2s"
        ]), 1)
        self.assertEqual(solution(lines=[
            "2016-09-15 01:00:04.002 2.0s",
            "2016-09-15 01:00:07.000 2s"
        ]), 2)
        self.assertEqual(solution(lines=[
            "2016-09-15 20:59:57.421 0.351s",
            "2016-09-15 20:59:58.233 1.181s",
            "2016-09-15 20:59:58.299 0.8s",
            "2016-09-15 20:59:58.688 1.041s",
            "2016-09-15 20:59:59.591 1.412s",
            "2016-09-15 21:00:00.464 1.466s",
            "2016-09-15 21:00:00.741 1.581s",
            "2016-09-15 21:00:00.748 2.31s",
            "2016-09-15 21:00:00.966 0.381s",
            "2016-09-15 21:00:02.066 2.62s"
        ]), 7)


if __name__ == "__main__":
    unittest.main()
