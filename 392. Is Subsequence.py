"""
https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false

"""


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        i = 0
        count = 0

        for num in s:
            while i < len(t):
                if t[i] == num:
                    count += 1
                    i += 1
                    break
                i += 1

        return count == len(s)


solution = Solution()

assert solution.isSubsequence('abc', 'ahbgdc') is True
assert solution.isSubsequence('axc', 'ahbgdc') is False
assert solution.isSubsequence('aaaaaa', 'bbaaaa') is False
