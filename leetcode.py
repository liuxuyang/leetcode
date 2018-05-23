def twoSum(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        """
    temp = dict()
    for i in xrange(len(nums)):
        if (target - nums[i]) in temp.keys():
            return [temp[target - nums[i]], i]
        temp[nums[i]] = i


def addTwoNumbers(l1, l2):
    """
        :type l1: List[int]
        :type l2: List[int]
        :rtype: List[int]

        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order and each of their nodes contain a single digit. 
        Add the two numbers and return it as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        """
    carry = 0
    out = []
    while l1 or l2 or carry:
        v1 = 0
        v2 = 0
        if l1:
            v1 = l1.pop()
        if l2:
            v2 = l2.pop()
        carry, v = divmod(v1 + v2 + carry, 10)
        out.append(v)
    return out


def lengthOfLongestSubstring(s):
    """
        :type s: str
        :rtype: int

        Given a string, find the length of the longest substring without repeating characters.
        """
    temp = out = ''
    d = {}
    for i in xrange(len(s)):
        if s[i] in temp:
            temp = s[d[s[i]] + 1:i]
        temp += s[i]
        d[s[i]] = i
        if len(out) < len(temp):
            out = temp
    return out


def findMedianSortedArrays(nums1, nums2):
    """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        There are two sorted arrays nums1 and nums2 of size m and n respectively.
        Find the median of the two sorted arrays. 
        The overall run time complexity should be O(log (m+n)).
        """
    m = len(nums1)
    n = len(nums2)