def solution(m, n, board):
    answer = 0
    erased = [[False] * len(board[0]) for _ in board]
    arr = [list(b) for b in board]
    rows = len(board)
    cols = len(board[0])
    while True:
        count = 0
        for i in range(rows - 1):
            for j in range(cols - 1):
                square_check(arr, erased, i, j)
        if count == 0:
            break
        else:
            answer += count
    print(arr)
    return answer


def square_check(arr, erased, i, j):
    pass


if __name__ == "__main__":
    m = 4
    n = 5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    print(solution(m, n, board))
