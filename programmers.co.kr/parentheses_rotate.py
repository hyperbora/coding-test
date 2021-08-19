"""
https://programmers.co.kr/learn/courses/30/lessons/76502
괄호 회전하기
"""


def solution(s):
    def is_match(target):
        stack = []
        left = ['[', '(', '{']
        right = [']', ')', '}']
        for cur in list(target):
            if cur in left:
                stack.append(cur)
            else:
                if not stack:
                    return 0
                last = stack.pop()
                index = left.index(last)
                if cur != right[index]:
                    return 0
        return 0 if stack else 1
    new_s = s * 2
    length = len(s)
    return sum([is_match(new_s[i: i + length]) for i in range(length)])


if __name__ == "__main__":
    print(solution("[](){}"))
    print(solution("}]()[{"))
    print(solution("[)(]"))
    print(solution("}}}"))
