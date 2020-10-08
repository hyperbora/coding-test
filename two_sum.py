import unittest

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        nums_dict = {}
        for (i, num) in enumerate(nums):
            if num in nums_dict:
                nums_dict[num].add(i)
            else:
                nums_dict[num] = set([i])
        for (k, v) in nums_dict.items():
            a = k
            b = target - a
            if b in nums_dict:
                temp_b = set(nums_dict[b])
                if a == b:
                    v1 = temp_b.pop()
                else:
                    temp_a = set(v)
                    v1 = temp_a.pop()
                try:
                    v2 = temp_b.pop()
                except KeyError:
                    pass
                else:
                    return [v1, v2]


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual([0, 1], sorted(s.twoSum(nums = [2,7,11,15], target = 9)))
        self.assertEqual([1, 2], sorted(s.twoSum(nums = [3,2,4], target = 6)))
        self.assertEqual([0, 1], sorted(s.twoSum(nums = [3,3], target = 6)))
        
if __name__ == "__main__":
    unittest.main()