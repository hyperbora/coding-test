"""
https://www.hackerrank.com/challenges/recursive-digit-sum/problem
"""

from collections import Counter


def superDigit(n, k):
    if len(n) == 1:
        return n

    def find_super_digit(num):
        if num // 10 < 1:
            return num
        c = Counter(list(str(num)))
        acc = 0
        for k, v in c.items():
            acc += int(k) * v
        return find_super_digit(acc)
    return find_super_digit(sum([int(i) for i in list(n)]) * k)


if __name__ == "__main__":
    print(superDigit('123', 3))
