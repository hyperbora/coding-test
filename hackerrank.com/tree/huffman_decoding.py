from collections import deque


class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None


def decodeHuff(root, s):
    decode = []
    q = deque(s)
    head = root
    while q:
        c = q.popleft()
        if c == '0':
            # left
            if head.left:
                head = head.left
            else:
                decode.append(head.data)
                head = root
                q.appendleft(c)
        else:
            # right
            if head.right:
                head = head.right
            else:
                decode.append(head.data)
                head = root
                q.appendleft(c)
    decode.append(head.data)
    print(''.join(decode))
