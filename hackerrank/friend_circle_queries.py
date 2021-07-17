#!/bin/python3

import os
from collections import deque, defaultdict


def calc_degree(graph, start):
    q = deque([start])
    visited = set([start])
    degree = 1
    while q:
        curr = q.popleft()
        for other in graph[curr]:
            if other not in visited:
                visited.add(other)
                degree += 1
                q.append(other)
    return degree

# Complete the maxCircle function below.


def maxCircle(queries):
    result = []
    graph = defaultdict(set)
    max_friend = 0
    for a, b in queries:
        if a not in graph and b not in graph:
            graph[a].add(b)
            graph[b].add(a)
            temp = 2
        else:
            graph[a].add(b)
            graph[b].add(a)
            temp = calc_degree(graph, a)
        max_friend = max(max_friend, temp)
        result.append(max_friend)
    return result


if __name__ == '__main__':

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    print('\n'.join(map(str, ans)))
