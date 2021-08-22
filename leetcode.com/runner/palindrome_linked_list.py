"""
런너(Runner)는 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법이다.
한 포인터가 다른 포인터보다 앞서게 하여 병합 지젖ㅁ이나 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있다.
일반적으로 빠른 런너(Fast Runner)는 두 칸씩 건너뛰고 느린 런너(Slow Runner)는 한 칸씩 이동하게 된다.
이때 빠른 런너가 연결 리스트의 끝에 도달하면, 느린 런너는 정확히 연결 리스트의 중간 지점을 가리키게 된다.
"""
from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 역순 링크드 리스트
        rev = None
        # 빠른 런너와 느린 런너의 초깃값은 head에서 시작한다.
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            # 빠른 런너는 두 칸씩, 느린 런너는 한 칸씩 이동
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        # 리스트의 길이가 홀수일 경우 다르게 처리해야 한다.
        # 중앙값은 팰린드롬 체크에서 배제되어야 하기 때문이다.
        # 이를 fast가 아직 None이 아니라는 경우로 간주할 수 있으며, slow를 한 칸 더 이동해 마무리한다.
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        # 정상적으로 비교가 되면 slow, rev 모두 끝까지 이동해 둘 다 None이 될 것이다.
        # 결과 확인은 not rev, not slow 모두 가능하다.
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

    class TestSolution(unittest.TestCase):
        def test_result(self):
            s = Solution()
            head = ListNode(val=1)
            head.next = ListNode(val=2)
            head.next.next = ListNode(val=2)
            head.next.next = ListNode(val=1)
            self.assertTrue(s.isPalindrome(head=head))
            head = ListNode(val=1)
            head.next = ListNode(val=2)
            self.assertFalse(s.isPalindrome(head=head))


if __name__ == "__main__":
    unittest.main()
