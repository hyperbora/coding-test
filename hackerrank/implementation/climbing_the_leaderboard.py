from bisect import bisect_left


def climbingLeaderboard(ranked, player):
    new_ranks = list(sorted(set(ranked)))
    length = len(new_ranks)
    answer = []
    for p in player:
        idx = bisect_left(new_ranks, p, 0, length)
        if idx == length:
            p_ranked = 1
            length += 1
            new_ranks.append(p)
        elif new_ranks[idx] == p:
            p_ranked = length - idx
        else:
            p_ranked = length + 1 - idx
            length += 1
            new_ranks.insert(idx, p)
        answer.append(p_ranked)
    return answer


if __name__ == '__main__':
    _ = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    _ = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    print('\n'.join(map(str, result)))
