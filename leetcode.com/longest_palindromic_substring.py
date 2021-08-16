import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = start
        mv = memoryview(s.encode())
        s_len = len(mv)
        max_length = 1

        i = 0
        while s_len - i > max_length and i < s_len:
            j = i + max_length + 1
            while j - i > max_length and j <= s_len:
                cur_length = j - i
                if cur_length > max_length and cur_length <= s_len:
                    half = cur_length // 2
                    if cur_length % 2 == 0:
                        head = mv[i:i + half]
                    else:
                        head = mv[i:i + half + 1]
                    tail = mv[j-1: i + half - 1: -1]
                    if head == tail:
                        max_length = cur_length
                        start = i
                        end = j
                j += 1
            i += 1
        rst = mv[start:end].tobytes().decode()
        if rst == '':
            return s[0]
        return rst


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual("bab", s.longestPalindrome("babad"))
        self.assertEqual("bb", s.longestPalindrome("cbbd"))
        self.assertEqual("a", s.longestPalindrome("a"))
        self.assertEqual("a", s.longestPalindrome("ac"))
        self.assertEqual("bb", s.longestPalindrome("bb"))
        self.assertEqual("xnnx", s.longestPalindrome("borcdubqiupahpwjizjjbkncelfazeqynfbrnzuvbhjnyvrlkdyfyjjxnprfocrmisugizsgvhszooktdwhehojbrdbtgkiwkhpfjfcstwcajiuediebdhukqnroxbgtvottummbypokdljjvnthcbesoyigscekrqswdpalnjnhcnqrarxuufzzmkwizptyvjhpfidgmskuaggtpxqisdlyloznkarxofzeeyvteynluofuhbllyiszszbwnsglqjkignusarxsjvctpgiwnhdufmfpanfwxjwlmhgllzsmdpncbwnsbdtsvrjybynifywkulqnzprcxockbhrhvnwxrkvwumyieazclcviumvormynbryaziijpdinwatwqppamfiqfiojgwkvfzyxadyfjrgmtttvlgkqghgbcfhkigfojjkhskzenlpasyozcsuccdxhulcubsgomvcrbqwakrraesfifecmoztayrdjicypakrrneulfbqqxtrdelggedvloebqaztmfyfkhuonrognejxpesmwgnmnnnamvkxqvzrgzdqtvuhccryeowywmbixktnkqnwzlzfvloyqcageugmjqihyjxhssmhkfzxpzxmgpjgsduogfolnkkqizitbvvgrkczmojxnabruwwzxxqcevdwvtiigwckpxnnxxxdhxpgomncttjutrsvyrqcfwxhexhaguddkiesmfrqfjfdaqbkeqinwicphktffuwcazlmerdhraufbpcznbuipmymipxbsdhuesmcwnkdvilqbnkaglloswcpqzdggnhjdkkumfuzihilrpcvemwllicoqiugobhrwdxtoefynqmccamhdtxujfudbglmiwqklriolqfkknbmindxtljulnxhipsieyohnczddabrxzjmompbtnnxvivmoyfzfrxlufowtqzojfclmatthjtbhotdoheusnpirwicbtyrcuojsdmfcx"))


if __name__ == "__main__":
    unittest.main()
