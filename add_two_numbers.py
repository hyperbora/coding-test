import unittest

class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return

def get_list_node(lst):
    output = None
    head = None
    for val in lst:
        node = ListNode(val=val)
        if head:
            head.next = node
            head = node
        else:
            output = node
            head = output
    return output

def print_list(list_node):
    head = list_node
    while head:
        print(head.val)
        head = head.next

class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual([0, 1], s.addTwoNumbers(nums = [2,7,11,15], target = 9))
        self.assertEqual([1, 2], s.addTwoNumbers(nums = [3,2,4], target = 6))
        self.assertEqual([0, 1], s.addTwoNumbers(nums = [3,3], target = 6))

if __name__ == "__main__":
    # unittest.main()
    lst = get_list_node([1, 2, 3])
    print_list(lst)
    lst = get_list_node([3, 2, 5])
    print_list(lst)