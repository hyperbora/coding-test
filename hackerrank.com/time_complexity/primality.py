import math

memo = {}


def primality(n):
    if n == 1:
        return "Not prime"
    if n == 2:
        return "Prime"
    if n in memo:
        return memo[n]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            memo[n] = "Not prime"
            break
    else:
        memo[n] = "Prime"
    return memo[n]
