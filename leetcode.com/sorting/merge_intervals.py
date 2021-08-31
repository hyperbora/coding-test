"""
https://leetcode.com/problems/merge-intervals/
겹치는 구간을 병한하라.
첫 번째 값을 기준으로 정렬한다.
현재 아이템의 시작이 이전 아이템의 끝과 겹치게 되면
끝나는 구간의 최대값을 기준으로 병합하는 형태로 계속 반복한다.
"""


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                # 콤마(,) 연산자
                # 리스트를 붙일 때 중첩 리스트로 만들어주는 역할을 한다.
                # merged += [i] 와 동일한 연산을 한다.
                merged += i,
        return merged
