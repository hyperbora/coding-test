"""
https://programmers.co.kr/learn/courses/30/lessons/1844
게임 맵 최단거리
"""
from collections import deque


def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    target = (rows - 1, cols - 1)
    visited = [[False] * cols for _ in range(rows)]
    q = deque([(0, 0, 1)])
    visited[0][0] = True

    dx = (-1, 0, 1, 0)
    dy = (0, -1, 0, 1)
    while q:
        i, j, cost = q.popleft()
        if (i, j) == target:
            return cost
        for x, y in zip(dx, dy):
            next_x = i + x
            next_y = j + y
            if 0 <= next_x < rows and 0 <= next_y < cols and not visited[next_x][next_y] and maps[next_x][next_y] == 1:
                q.append([next_x, next_y, cost + 1])
                visited[next_x][next_y] = True

    return -1


if __name__ == "__main__":
    maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
        1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
    print(solution(maps))
    maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
        1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
    print(solution(maps))
