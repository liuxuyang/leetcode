import unittest
from leetcode import *


class TestLeetCode(unittest.TestCase):
    def test_twoSum(self):
        nums = [2, 3, 8, 5, 11, 14, 16]
        target = 16
        self.assertEqual([3, 4], twoSum(nums, target))
        self.assertNotEqual([2, 2], twoSum(nums, target))

    def test_addTwoNumbers(self):
        self.assertEqual([7, 0, 8], addTwoNumbers([2, 4, 3], [5, 6, 4]))
        self.assertEqual([3, 1, 0, 1], addTwoNumbers([4, 3, 1], [5, 8, 2]))

    def test_lengthOfLongestSubstring(self):
        self.assertEqual("abc", lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual("b", lengthOfLongestSubstring("bbbbb"))
        self.assertEqual("wke", lengthOfLongestSubstring("pwwkew"))
        self.assertEqual("bac", lengthOfLongestSubstring("abbbac"))
        self.assertEqual("bacsd", lengthOfLongestSubstring("abbbacsdae"))
        self.assertEqual(
            "sdgfjyuqwe",
            lengthOfLongestSubstring(
                "pwwkewaskjdhakjgfhasjbrkasjgfkajsdbnjadghjsdgfjyuqwe"))

    # def test_findMedianSortedArrays(self):
    #     self.assertEqual(2.0, findMedianSortedArrays([1, 3], [2]))
    #     self.assertEqual(2.5, findMedianSortedArrays([1, 2], [3, 4]))


if __name__ == "__main__":
    unittest.main()