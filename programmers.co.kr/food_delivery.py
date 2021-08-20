"""
https://programmers.co.kr/learn/courses/30/lessons/12978
배달
"""
import heapq
from collections import defaultdict

INF = 50 * 10_000


def solution(N, road, K):
    graph = defaultdict(list)
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    q = []
    start = 1
    heapq.heappush(q, (0, start))
    distance = [INF] * (N + 1)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return len([d for d in distance if d <= K])


if __name__ == "__main__":
    N = 5
    road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
    K = 3
    print(solution(N, road, K))
    N = 6
    road = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
        3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
    K = 4
    print(solution(N, road, K))
