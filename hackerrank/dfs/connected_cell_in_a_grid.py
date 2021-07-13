"""
https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem
"""


def print_array(arr, row, col):
    for i in range(row):
        for j in range(col):
            print(arr[i][j], end=" ")
        print()


def maxRegion(grid, row, col):
    visited = [[False] * col for _ in range(row)]
    answer = 0
    direction = [(i, j) for i in range(-1, 2)
                 for j in range(-1, 2) if i != 0 or j != 0]
    double_direction = [(i, j) for i in range(-2, 3)
                        for j in range(-2, 3) if i != 0 or j != 0]
    for r in range(row):
        for c in range(col):
            if not visited[r][c] and grid[r][c] == 1:
                stack = []
                stack.append((r, c))
                count = 0
                while stack:
                    i, j = stack.pop()
                    if not visited[i][j] and grid[i][j] == 1:
                        visited[i][j] = True
                        count += 1
                        for x, y in direction:
                            if 0 <= i + x < row and 0 <= j + y < col and grid[i + x][j + y] == 1:
                                stack.append((i + x, j + y))
                if count == 1:
                    valid = True
                    for x, y in double_direction:
                        if 0 <= r + x < row and 0 <= c + y < col and grid[r + x][c + y] == 1:
                            valid = False
                            break
                    if valid:
                        for x, y in direction:
                            if 0 <= r + x < row and 0 <= c + y < col and grid[r + x][c + y] == 0:
                                count += 1
                if answer < count:
                    answer = count
    return answer


if __name__ == "__main__":
    '''
    1 1 0 0
    0 1 1 0
    0 0 1 0
    1 0 0 0
    '''
    # row = int(input())
    # col = int(input())
    # arr = []
    # for i in range(row):
    #     arr.append(list(map(int, input().strip().split())))
    # print(maxRegion(arr, row, col))
    arr = [
        [1, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 0]
    ]
    row = 7
    col = 8
    print(maxRegion(arr, row, col))
